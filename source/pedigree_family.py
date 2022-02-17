from pedigree_fields import Role
from pedigree_units import Individual
from pedigree_units import MatingUnit
from pedigree_units import SibshipUnit


class PedigreeFamily:
    def __init__(self, pedigree_identifier) -> None:
        try:
            assert isinstance(pedigree_identifier, str)
        except AssertionError:
            raise AssertionError('The pedigree identifier is invalid!')

        self.__pedigree_identifier = pedigree_identifier

        self.__pedigree_individuals = dict()
        self.__pedigree_mating_units = dict()
        self.__pedigree_sibship_units = dict()

        self.__min_generation_rank = None
        self.__max_generation_rank = None


    @property
    def pedigree_identifier(self) -> str:
        return self.__pedigree_identifier


    @property
    def pedigree_individuals(self) -> dict:
        return self.__pedigree_individuals


    @property
    def pedigree_mating_units(self) -> dict:
        return self.__pedigree_mating_units


    @property
    def pedigree_sibship_units(self) -> dict:
        return self.__pedigree_sibship_units


    @property
    def min_generation_rank(self):
        return self.__min_generation_rank


    @property
    def max_generation_rank(self):
        return self.__max_generation_rank


    @pedigree_identifier.deleter
    def pedigree_identifier(self) -> None:
        del self.__pedigree_identifier


    @pedigree_individuals.deleter
    def pedigree_individuals(self) -> None:
        del self.__pedigree_individuals

    
    @pedigree_mating_units.deleter
    def pedigree_mating_units(self) -> None:
        del self.__pedigree_mating_units


    @pedigree_sibship_units.deleter
    def pedigree_sibship_units(self) -> None:
        del self.__pedigree_sibship_units


    @min_generation_rank.deleter
    def min_generation_rank(self) -> None:
        del self.__min_generation_rank


    @max_generation_rank.deleter
    def max_generation_rank(self) -> None:
        del self.__max_generation_rank


    def __hash__(self):
        return hash(self.pedigree_identifier)


    def __eq__(self, pedigree_family):
        if not isinstance(pedigree_family, PedigreeFamily):
            return False
        return self.__hash__() == pedigree_family.__hash__()


    def __repr__(self) -> str:
        return self.pedigree_identifier


    def __del__(self) -> None:
        del self.__pedigree_identifier

        del self.__pedigree_individuals
        del self.__pedigree_mating_units
        del self.__pedigree_sibship_units
        
        del self.__min_generation_rank
        del self.__max_generation_rank


    def add_individual(self, individual):
        print(type(individual))
        assert isinstance(individual, Individual)
        key = individual.individual_identifier
        self.__pedigree_individuals[key] = individual


    def add_mating_unit(self, mating_unit):
        assert isinstance(mating_unit, MatingUnit)
        key = mating_unit.__repr__
        self.__pedigree_mating_units[key] = mating_unit


    def add_sibship_unit(self, sibship_unit):
        assert isinstance(sibship_unit, SibshipUnit)
        key = sibship_unit.__repr__
        self.__pedigree_sibship_units[key] = sibship_unit


    def build_mating_units(self):
        for individual in self.pedigree_individuals:
            current_individual = self.pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)

            if current_individual.individual_father != '0' and current_individual.individual_mother != '0':
                father = self.pedigree_individuals[current_individual.individual_father]
                mother = self.pedigree_individuals[current_individual.individual_mother]

                current_mating_unit = MatingUnit(self.pedigree_identifier, father, mother, None)
                current_sibship_unit = SibshipUnit(self.pedigree_identifier, current_mating_unit)
                current_mating_unit = MatingUnit(self.pedigree_identifier, father, mother, current_sibship_unit)

                self.pedigree_mating_units[str(current_mating_unit)]    = current_mating_unit
                self.pedigree_sibship_units[str(current_sibship_unit)]  = current_sibship_unit

                current_individual.mating_unit_relation     = self.pedigree_mating_units[str(current_mating_unit)]
                current_individual.sibship_unit_relation    = self.pedigree_sibship_units[str(current_mating_unit.sibship_unit_relation)]

        for individual in self.pedigree_individuals:
            current_individual = self.pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)

            for mating_unit in self.pedigree_mating_units:
                current_mating_unit = self.pedigree_mating_units[mating_unit]
                assert isinstance(current_mating_unit, MatingUnit)

                if  current_individual == current_mating_unit.male_mate_individual or \
                    current_individual == current_mating_unit.female_mate_individual:
                    current_individual.mating_instances.append(current_mating_unit)


    def build_sibship_units(self):
        for sibship_unit in self.pedigree_sibship_units:
            current_sibship_unit = self.pedigree_sibship_units[sibship_unit]
            assert isinstance(current_sibship_unit, SibshipUnit)

            for individual in self.pedigree_individuals:
                current_individual = self.pedigree_individuals[individual]
                assert isinstance(current_individual, Individual)

                if current_individual.sibship_unit_relation != None:
                    if current_individual.sibship_unit_relation == current_sibship_unit:
                        current_sibship_unit.add_sibling_individual(current_individual)
                        current_individual.sibship_unit_relation = current_sibship_unit


    def get_proband(self):
        for individual in self.pedigree_individuals:
            current_individual = self.pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)

            if current_individual.individual_role == Role.PROBAND:
                current_individual.generation_rank = 0
                return current_individual

        return None


    def validate_propagated_rank(self):
        for individual in self.__pedigree_individuals:
            current_individual = self.__pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)

            if current_individual.generation_rank is None:
                return False

        return True


    def build_generation_rank(self):
        touched_individuals = []
        touched_individuals.append(self.get_proband())

        while self.validate_propagated_rank() is False:
            next_touched_individuals = []
            last_touched_individuals = []

            for individual in touched_individuals:
                assert isinstance(individual, Individual)

                for sibship_unit in self.pedigree_sibship_units:
                    current_sibship_unit = self.pedigree_sibship_units[sibship_unit]
                    assert isinstance(current_sibship_unit, SibshipUnit)

                    if individual.sibship_unit_relation == current_sibship_unit:
                        for i in range(len(current_sibship_unit.siblings_individuals)):
                            sibling = current_sibship_unit.siblings_individuals[i]
                            assert isinstance(sibling, Individual)

                            if individual != sibling and sibling.generation_rank is None:
                                sibling.generation_rank = individual.generation_rank
                                current_sibship_unit.change_sibling_individual(sibling, i)
                                next_touched_individuals.append(sibling)
                        break

                for mating_unit in self.pedigree_mating_units:
                    current_mating_unit = self.pedigree_mating_units[mating_unit]
                    assert isinstance(current_mating_unit, MatingUnit)

                    if individual.mating_unit_relation == current_mating_unit:
                        if current_mating_unit.male_mate_individual.generation_rank is None:
                            current_mating_unit.male_mate_individual.generation_rank    = individual.generation_rank - 1
                            next_touched_individuals.append(current_mating_unit.male_mate_individual)
                        
                        if current_mating_unit.female_mate_individual.generation_rank is None:
                            current_mating_unit.female_mate_individual.generation_rank  = individual.generation_rank - 1
                            next_touched_individuals.append(current_mating_unit.female_mate_individual)


                for mating_unit in self.pedigree_mating_units:
                    current_mating_unit = self.pedigree_mating_units[mating_unit]
                    assert isinstance(current_mating_unit, MatingUnit)

                    if  individual == current_mating_unit.male_mate_individual or \
                        individual == current_mating_unit.female_mate_individual:
                        assert isinstance(current_mating_unit.sibship_unit_relation, SibshipUnit)

                        for i in range(len(current_mating_unit.sibship_unit_relation.siblings_individuals)):
                            sibling = current_mating_unit.sibship_unit_relation.siblings_individuals[i]
                            assert isinstance(sibling, Individual)

                            if sibling.generation_rank is None:
                                sibling.generation_rank = individual.generation_rank + 1
                                current_mating_unit.sibship_unit_relation.change_sibling_individual(sibling, i)
                                next_touched_individuals.append(sibling)

                for mating_unit in self.pedigree_mating_units:
                    current_mating_unit = self.pedigree_mating_units[mating_unit]
                    assert isinstance(current_mating_unit, MatingUnit)

                    if  individual == current_mating_unit.male_mate_individual and \
                        current_mating_unit.female_mate_individual.generation_rank is None:
                        current_mating_unit.female_mate_individual.generation_rank = individual.generation_rank
                        next_touched_individuals.append(current_mating_unit.female_mate_individual)
                    elif individual == current_mating_unit.female_mate_individual and \
                        current_mating_unit.male_mate_individual.generation_rank is None:
                        current_mating_unit.male_mate_individual.generation_rank = individual.generation_rank
                        next_touched_individuals.append(current_mating_unit.male_mate_individual)

                last_touched_individuals.append(individual)

            touched_individuals = next_touched_individuals

        self.transform_generation_rank()

        for mating_unit in self.pedigree_mating_units:
            current_mating_unit = self.pedigree_mating_units[mating_unit]
            assert isinstance(current_mating_unit, MatingUnit)

            if  current_mating_unit.male_mate_individual.generation_rank == \
                current_mating_unit.female_mate_individual.generation_rank:
                current_mating_unit.generation_rank = current_mating_unit.male_mate_individual.generation_rank

        for sibship_unit in self.pedigree_sibship_units:
            current_sibship_unit = self.pedigree_sibship_units[sibship_unit]
            assert isinstance(current_sibship_unit, SibshipUnit)
            sibling = current_sibship_unit.siblings_individuals[0]
            assert isinstance(sibling, Individual)
            current_sibship_unit.generation_rank = sibling.generation_rank

    def transform_generation_rank(self):
        generation_ranks = list()

        for individual in self.pedigree_individuals:
            current_individual = self.pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)
            generation_ranks.append(current_individual.generation_rank)

        difference_rank = max(generation_ranks) - min(generation_ranks)
        self.__min_generation_rank = 1
        self.__max_generation_rank = difference_rank + 1

        for individual in self.pedigree_individuals:
            current_individual = self.pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)
            current_individual.generation_rank = current_individual.generation_rank + difference_rank + 1


    def build_extended_sibship_units(self):
        for key_sibship in self.pedigree_sibship_units:
            sibship_unit = self.pedigree_sibship_units[key_sibship]
            assert isinstance(sibship_unit, SibshipUnit)

            for sibling in sibship_unit.siblings_individuals:
                for key_mating in self.pedigree_mating_units:
                    mating_unit = self.pedigree_mating_units[key_mating]
                    assert isinstance(mating_unit, MatingUnit)

                    if  sibling == mating_unit.male_mate_individual:
                        condition1 = mating_unit.female_mate_individual.individual_father == '0'
                        condition2 = mating_unit.female_mate_individual.individual_mother == '0'

                        if condition1 and condition2:
                            sibship_unit.add_sibling_individual_mate(mating_unit.female_mate_individual)
                    
                    if  sibling == mating_unit.female_mate_individual:
                        condition1 = mating_unit.male_mate_individual.individual_father == '0'
                        condition2 = mating_unit.male_mate_individual.individual_mother == '0'

                        if condition1 and condition2:
                            sibship_unit.add_sibling_individual_mate(mating_unit.male_mate_individual)
                            

    def get_individuals_by_generation(self, generation_rank):
        generation_individuals = []

        for key in self.pedigree_individuals:
            individual = self.pedigree_individuals[key]
            assert isinstance(individual, Individual)
            
            if individual.generation_rank == generation_rank:
                generation_individuals.append(individual)

        return generation_individuals

    def print_pedigree_family_data(self):
        print("Pedigree Family:", self.pedigree_identifier)

        for key in self.pedigree_individuals:
            individual = self.pedigree_individuals[key]
            assert isinstance(individual, Individual)
            print("Individual:", individual, individual.generation_rank)

        for key in self.pedigree_mating_units:
            mating_unit = self.pedigree_mating_units[key]
            assert isinstance(mating_unit, MatingUnit)
            print("Mating Unit:", mating_unit, mating_unit.generation_rank)

        for key in self.pedigree_sibship_units:
            sibship_unit = self.pedigree_sibship_units[key]
            assert isinstance(sibship_unit, SibshipUnit)
            print("Sibship Unit:", sibship_unit, sibship_unit.generation_rank)
