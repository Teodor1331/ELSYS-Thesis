# This Python file uses the following encoding: UTF-8

"""The module has the class Pedigree Family.

This module contains the class for the pedigree family
that manages the whole pedigree structure.
"""

from typing import Union
from typing import TypeVar
from typing import Generic

from .pedigree_fields import Role
from .pedigree_units import Individual
from .pedigree_units import MatingUnit
from .pedigree_units import SibshipUnit

PedigreeFamilyBase = TypeVar('PedigreeFamilyBase')


class PedigreeFamily(Generic[PedigreeFamilyBase]):
    """Class Name: Pedigree Family.

    This class is used to manage the
    whole structure of a single pedigree.
    """

    __pedigree_identifier: str
    __pedigree_individuals: dict
    __pedigree_mating_units: dict
    __pedigree_sibship_units: dict
    __min_generation_rank: int
    __max_generation_rank: int

    def __init__(self, pedigree_identifier) -> None:
        """Initialize an instance of the PedigreeFamily class.

        Parameters: The pedigree identifier of the pedigree.
        """
        try:
            assert isinstance(pedigree_identifier, str)
        except AssertionError as assertion_error:
            message = 'The pedigree family constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__pedigree_identifier = pedigree_identifier

        self.__pedigree_individuals = {}
        self.__pedigree_mating_units = {}
        self.__pedigree_sibship_units = {}

        self.__min_generation_rank = 0
        self.__max_generation_rank = 0

    @property
    def pedigree_identifier(self) -> str:
        """Return the pedigree identifier property of the class."""
        return self.__pedigree_identifier

    @property
    def pedigree_individuals(self) -> dict:
        """Return the pedigree individuals property of the class."""
        return self.__pedigree_individuals

    @property
    def pedigree_mating_units(self) -> dict:
        """Return the pedigree mating units property of the class."""
        return self.__pedigree_mating_units

    @property
    def pedigree_sibship_units(self) -> dict:
        """Return the pedigree sibship units property of the class."""
        return self.__pedigree_sibship_units

    @property
    def min_generation_rank(self) -> int:
        """Return the min generation rank property of the class."""
        return self.__min_generation_rank

    @property
    def max_generation_rank(self) -> int:
        """Return the max generation rank property of the class."""
        return self.__max_generation_rank

    def __hash__(self) -> int:
        return hash(self.pedigree_identifier)

    def __eq__(self, pedigree_family: PedigreeFamilyBase) -> bool:
        if not isinstance(pedigree_family, PedigreeFamily):
            return False
        return self.__hash__() == pedigree_family.__hash__()

    def __repr__(self) -> str:
        return self.pedigree_identifier

    def add_individual(self, individual: Individual) -> None:
        """Add Individual instance to the individuals' collection."""
        assert isinstance(individual, Individual)
        key = individual.individual_identifier
        self.__pedigree_individuals[key] = individual

    def add_mating_unit(self, mating_unit: Individual) -> None:
        """Add Mating Unit instance to the mating units' collection."""
        assert isinstance(mating_unit, MatingUnit)
        key = mating_unit.__repr__
        self.__pedigree_mating_units[key] = mating_unit

    def add_sibship_unit(self, sibship_unit: Individual) -> None:
        """Add Sibship Unit instance to the sibship units' collection."""
        assert isinstance(sibship_unit, SibshipUnit)
        key = sibship_unit.__repr__
        self.__pedigree_sibship_units[key] = sibship_unit

    def build_mating_units(self) -> None:
        """Build all the mating units in the pedigree structure.

        The method iterates through all the individuals and builds
        the needed mating units and creates an empty linked instances
        of the sibships units, corresponding to the respective mating
        units. At the end, the mating units are added to the individuals
        mating units collections, where the individual has taken part
        in the respective mating unit.
        """
        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)

            condition1 = individual[1].individual_father != '0'
            condition2 = individual[1].individual_mother != '0'

            if condition1 and condition2:
                father = self.pedigree_individuals[individual[1].individual_father]
                mother = self.pedigree_individuals[individual[1].individual_mother]

                mating_unit = MatingUnit(self.pedigree_identifier, father, mother)
                sibship_unit = SibshipUnit(self.pedigree_identifier, mating_unit)
                mating_unit = MatingUnit(self.pedigree_identifier, father, mother, sibship_unit)

                self.pedigree_mating_units[str(mating_unit)] = mating_unit
                self.pedigree_sibship_units[str(sibship_unit)] = sibship_unit

                individual[1].mating_unit_relation = self.pedigree_mating_units[str(mating_unit)]
                individual[1].sibship_unit_relation = self.pedigree_sibship_units[
                    str(mating_unit.sibship_unit_relation)]

        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)

            for mating_unit in self.pedigree_mating_units.items():
                assert isinstance(mating_unit[1], MatingUnit)

                if individual[1] == mating_unit[1].male_mate_individual or \
                        individual[1] == mating_unit[1].female_mate_individual:
                    individual[1].mating_instances.append(mating_unit[1])

    def build_sibship_units(self) -> None:
        """Build all the sibship units in the pedigree structure.

        The method uses the already created sibship units without data
        and simply adds the needed individuals to the corresponding
        sibships.
        """
        for sibship_unit in self.pedigree_sibship_units.items():
            assert isinstance(sibship_unit[1], SibshipUnit)

            for individual in self.pedigree_individuals.items():
                assert isinstance(individual[1], Individual)

                if individual[1].sibship_unit_relation is not None:
                    if individual[1].sibship_unit_relation == sibship_unit[1]:
                        sibship_unit[1].add_sibling_individual(individual[1])
                        individual[1].sibship_unit_relation = sibship_unit[1]

    def get_proband(self) -> Union[Individual, None]:
        """Get the proband individual.

        The method find the proband in the pedigree structure.
        Returns an Individual instance if such a proband exists
        in the pedigree. If not, return None as a result.
        """
        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)

            if individual[1].individual_role == Role.PROBAND:
                individual[1].generation_rank = 0
                return individual[1]

        return None

    def validate_propagated_rank(self) -> bool:
        """Validate if the generation rank is propagated.

        This method checks if every individual in the
        pedigree has an attached generation rank.
        """
        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)

            if individual[1].generation_rank is None:
                return False

        return True

    def build_generation_rank(self) -> None:
        """Build the generation rank for all the base units.

        The method attach a generation rank to all the
        base units in the pedigree structure according
        to the strategy:
            1. Siblings - first given
            2. Parents - second given
            3. Children - third given
            4. Mates - fourth given
        At the end, the method attach a generation rank
        to the mating units and the sibship units.
        """
        touched_individuals = [self.get_proband()]

        while self.validate_propagated_rank() is False:
            next_touched_individuals = []
            last_touched_individuals = []

            for individual in touched_individuals:
                assert isinstance(individual, Individual)

                for sibship_unit in self.pedigree_sibship_units.items():
                    assert isinstance(sibship_unit[1], SibshipUnit)

                    if individual.sibship_unit_relation == sibship_unit[1]:
                        for i, _ in enumerate(sibship_unit[1].siblings_individuals):
                            sibling = sibship_unit[1].siblings_individuals[i]
                            assert isinstance(sibling, Individual)

                            if individual != sibling and sibling.generation_rank is None:
                                sibling.generation_rank = individual.generation_rank
                                sibship_unit[1].change_sibling_individual(sibling, i)
                                next_touched_individuals.append(sibling)
                        break

                for mating_unit in self.pedigree_mating_units.items():
                    assert isinstance(mating_unit[1], MatingUnit)

                    if individual.mating_unit_relation == mating_unit[1]:
                        if mating_unit[1].male_mate_individual.generation_rank is None:
                            mating_unit[1].male_mate_individual.generation_rank = individual.generation_rank - 1
                            next_touched_individuals.append(mating_unit[1].male_mate_individual)

                        if mating_unit[1].female_mate_individual.generation_rank is None:
                            mating_unit[1].female_mate_individual.generation_rank = individual.generation_rank - 1
                            next_touched_individuals.append(mating_unit[1].female_mate_individual)

                for mating_unit in self.pedigree_mating_units.items():
                    assert isinstance(mating_unit[1], MatingUnit)

                    if individual in (mating_unit[1].male_mate_individual,
                       mating_unit[1].female_mate_individual):
                        assert isinstance(mating_unit[1].sibship_unit_relation, SibshipUnit)

                        for i, _ in enumerate(mating_unit[1].sibship_unit_relation.siblings_individuals):
                            sibling = mating_unit[1].sibship_unit_relation.siblings_individuals[i]
                            assert isinstance(sibling, Individual)

                            if sibling.generation_rank is None:
                                sibling.generation_rank = individual.generation_rank + 1
                                mating_unit[1].sibship_unit_relation.change_sibling_individual(sibling, i)
                                next_touched_individuals.append(sibling)

                for mating_unit in self.pedigree_mating_units.items():
                    assert isinstance(mating_unit[1], MatingUnit)

                    if individual == mating_unit[1].male_mate_individual and \
                            mating_unit[1].female_mate_individual.generation_rank is None:
                        mating_unit[1].female_mate_individual.generation_rank = individual.generation_rank
                        next_touched_individuals.append(mating_unit[1].female_mate_individual)
                    elif individual == mating_unit[1].female_mate_individual and \
                            mating_unit[1].male_mate_individual.generation_rank is None:
                        mating_unit[1].male_mate_individual.generation_rank = individual.generation_rank
                        next_touched_individuals.append(mating_unit[1].male_mate_individual)

                last_touched_individuals.append(individual)

            touched_individuals = next_touched_individuals

        self.transform_generation_rank()

        for mating_unit in self.pedigree_mating_units.items():
            assert isinstance(mating_unit[1], MatingUnit)

            if mating_unit[1].male_mate_individual.generation_rank == \
                    mating_unit[1].female_mate_individual.generation_rank:
                mating_unit[1].generation_rank = mating_unit[1].male_mate_individual.generation_rank

        for sibship_unit in self.pedigree_sibship_units.items():
            assert isinstance(sibship_unit[1], SibshipUnit)
            sibling = sibship_unit[1].siblings_individuals[0]
            assert isinstance(sibling, Individual)
            sibship_unit[1].generation_rank = sibling.generation_rank

    def transform_generation_rank(self) -> None:
        """Transform the generation rank.

        This method transforms the values of all the
        generation ranks to valid ones and sets the
        min and max one in the whole pedigree.
        """
        generation_ranks = []

        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)
            generation_ranks.append(individual[1].generation_rank)

        difference_rank = max(generation_ranks) - min(generation_ranks)
        self.__min_generation_rank = 1
        self.__max_generation_rank = difference_rank + 1

        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)
            individual[1].generation_rank += difference_rank

    def build_extended_sibship_units(self) -> None:
        """Build all the extended sibship units in the pedigree structure.

        The method uses the already created sibship units with the
        siblings data and fills them with the additional data for
        the orphan spouses of the corresponding siblings in the sibship.
        """
        for sibship_unit in self.pedigree_sibship_units.items():
            assert isinstance(sibship_unit[1], SibshipUnit)
            for sibling in sibship_unit[1].siblings_individuals:
                for mating_unit in self.pedigree_mating_units.items():
                    assert isinstance(mating_unit[1], MatingUnit)

                    if sibling == mating_unit[1].male_mate_individual:
                        condition1 = mating_unit[1].female_mate_individual.individual_father == '0'
                        condition2 = mating_unit[1].female_mate_individual.individual_mother == '0'

                        if condition1 and condition2:
                            sibship_unit[1].add_sibling_individual_mate(mating_unit[1].female_mate_individual)

                    if sibling == mating_unit[1].female_mate_individual:
                        condition1 = mating_unit[1].male_mate_individual.individual_father == '0'
                        condition2 = mating_unit[1].male_mate_individual.individual_mother == '0'

                        if condition1 and condition2:
                            sibship_unit[1].add_sibling_individual_mate(mating_unit[1].male_mate_individual)

    def get_individuals_by_generation(self, generation_rank: int) -> list:
        """Get all individuals by a given generation.

        This method gets a whole generation by a given
        generation rank. Returns the list with the
        corresponding individuals from the generation.
        """
        generation_individuals = []

        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)

            if individual[1].generation_rank == generation_rank:
                generation_individuals.append(individual[1])

        return generation_individuals

    def collect_mating_units_for_individuals(self) -> None:
        """Collect the mating units for the individuals.

        This method fixes if one of the mating units has not been
        correctly associated to the individual, which take part in
        the mating.
        """
        for individual in self.pedigree_individuals.items():
            for mating_unit in self.pedigree_mating_units.items():
                assert isinstance(individual[1], Individual)
                assert isinstance(mating_unit[1], MatingUnit)

                condition1 = mating_unit[1].male_mate_individual == individual
                condition2 = mating_unit[1].female_mate_individual == individual

                if condition1 or condition2:
                    if mating_unit not in individual[1].mating_instances:
                        individual[1].mating_instances.append(mating_unit)

    def print_pedigree_family_data(self) -> None:
        """Print the data for the pedigree.

        The method can be used to print the data
        from the inner structure of the pedigree.
        """
        print("Pedigree Family:", self.pedigree_identifier)

        for individual in self.pedigree_individuals.items():
            assert isinstance(individual[1], Individual)
            print("Individual:", individual[1], individual[1].generation_rank)

        for mating_unit in self.pedigree_mating_units.items():
            assert isinstance(mating_unit[1], MatingUnit)
            print("Mating Unit:", mating_unit[1], mating_unit[1].generation_rank)

        for sibship_unit in self.pedigree_sibship_units.items():
            assert isinstance(sibship_unit[1], SibshipUnit)
            print("Sibship Unit:", sibship_unit[1], sibship_unit[1].generation_rank)
