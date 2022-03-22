# This Python file uses the following encoding: UTF-8

"""The module has the classes Individual, MatingUnit and SibshipUnit.

This module contains classes for the base pedigree units.
Every base unit is created with its own specifications.
"""

from typing import Union
from typing import TypeVar
from typing import Generic

from .pedigree_fields import Sex
from .pedigree_fields import Status
from .pedigree_fields import Role

IndividualBase = TypeVar('IndividualBase')
MatingUnitBase = TypeVar('MatingUnitBase')
SibshipUnitBase = TypeVar('SibshipUnitBase')


class Individual(Generic[IndividualBase]):
    """Class Name: Individual.

    This class is used to manage the
    base unit of a single individual
    in the structure of the pedigree.
    """

    __pedigree_identifier: str
    __individual_identifier: str
    __individual_father: str
    __individual_mother: str
    __individual_sex: Sex
    __individual_status: Status
    __individual_role: Role
    __mating_unit_relation: Union[MatingUnitBase, None]
    __sibship_unit_relation: Union[SibshipUnitBase, None]
    __generation_rank: Union[int, None]
    __mating_instances: list

    def __init__(self, individual_data) -> None:
        """Initialize an instance of the Individual class.

        Parameters: The individual data for the individual.
        """
        try:
            assert isinstance(individual_data, list)
        except AssertionError as assertion_error:
            message = 'The individual constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__pedigree_identifier = individual_data[0]
        self.__individual_identifier = individual_data[1]
        self.__individual_father = individual_data[2]
        self.__individual_mother = individual_data[3]

        self.__individual_sex = Individual.decide_sex_individual(individual_data[4])
        self.__individual_status = Individual.decide_status_individual(individual_data[5])
        self.__individual_role = Individual.decide_role_individual(individual_data[6])

        self.__mating_unit_relation = None
        self.__sibship_unit_relation = None

        self.__generation_rank = None
        self.__mating_instances = []

    @property
    def pedigree_identifier(self) -> str:
        """Return the pedigree identifier property of the class."""
        return self.__pedigree_identifier

    @property
    def individual_identifier(self) -> str:
        """Return the individual identifier property of the class."""
        return self.__individual_identifier

    @property
    def individual_father(self) -> str:
        """Return the individual father property of the class."""
        return self.__individual_father

    @property
    def individual_mother(self) -> str:
        """Return the individual mother property of the class."""
        return self.__individual_mother

    @property
    def individual_sex(self) -> Sex:
        """Return the individual sex property of the class."""
        return self.__individual_sex

    @property
    def individual_status(self) -> Status:
        """Return the individual status property of the class."""
        return self.__individual_status

    @property
    def individual_role(self) -> Role:
        """Return the individual role property of the class."""
        return self.__individual_role

    @property
    def mating_unit_relation(self) -> Union[MatingUnitBase, None]:
        """Return the mating unit relation property of the class."""
        return self.__mating_unit_relation

    @property
    def sibship_unit_relation(self) -> Union[SibshipUnitBase, None]:
        """Return the sibship unit relation property of the class."""
        return self.__sibship_unit_relation

    @property
    def generation_rank(self) -> Union[int, None]:
        """Return the generation rank property of the class."""
        return self.__generation_rank

    @property
    def mating_instances(self) -> list:
        """Return the mating instances property of the class."""
        return self.__mating_instances

    @mating_unit_relation.setter
    def mating_unit_relation(self, mating_unit_relation) -> None:
        assert isinstance(mating_unit_relation, MatingUnit)
        self.__mating_unit_relation = mating_unit_relation

    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation) -> None:
        assert isinstance(sibship_unit_relation, SibshipUnit)
        self.__sibship_unit_relation = sibship_unit_relation

    @generation_rank.setter
    def generation_rank(self, generation_rank) -> None:
        assert isinstance(generation_rank, int)
        self.__generation_rank = generation_rank

    @mating_instances.setter
    def mating_instances(self, mating_instances) -> None:
        self.__mating_instances = mating_instances

    def __hash__(self) -> int:
        return hash(self.pedigree_identifier) + \
                hash(self.individual_identifier)

    def __eq__(self, individual) -> bool:
        if not isinstance(individual, Individual):
            return False
        return self.__hash__() == individual.__hash__()

    def __repr__(self) -> str:
        return self.individual_identifier

    @staticmethod
    def decide_sex_individual(string) -> Sex:
        """Decide the sex of the individual.

        Accepts: String - the value of the sex.
        Returns: A value from the Sex Enum Type.
        """
        try:
            assert isinstance(string, str)
        except AssertionError as assertion_error:
            message = 'The given argument is not a string!'
            raise AssertionError(message) from assertion_error

        if string == '0':
            return Sex.UNKNOWN

        return Sex.MALE if string == '1' else Sex.FEMALE

    @staticmethod
    def decide_status_individual(string) -> Status:
        """Decide the status of the individual.

        Accepts: String - the value of the status.
        Returns: A value from the Status Enum Type.
        """
        try:
            assert isinstance(string, str)
        except AssertionError as assertion_error:
            message = 'The given argument is not a string!'
            raise AssertionError(message) from assertion_error

        if string == '0':
            return Status.UNKNOWN

        return Status.UNAFFECTED if string == '1' else Status.AFFECTED

    @staticmethod
    def decide_role_individual(string) -> Role:
        """Decide the role of the individual.

        Accepts: String - the value of the role.
        Returns: A value from the Role Enum Type.
        """
        try:
            assert isinstance(string, str)
        except AssertionError as assertion_error:
            message = 'The given argument is not a string!'
            raise AssertionError(message) from assertion_error

        if string == 'prb':
            return Role.PROBAND

        return Role.__members__[string.upper()] \
            if string != 'null' else Sex.UNKNOWN

    def has_parents(self) -> bool:
        """Check if the individual has parents.

        Accepts: No arguments.
        Returns: Boolean result.
        """
        condition1 = self.individual_father != '0'
        condition2 = self.individual_mother != '0'
        return condition1 and condition2

    def are_mates(self, mate) -> bool:
        """Check if two individuals are mates.

        Accepts: Possible mate of type Individual.
        Returns: Boolean result.
        """
        assert isinstance(mate, Individual)

        for mating_instance in self.mating_instances:
            assert isinstance(mating_instance, MatingUnit)

            male_mate = mating_instance.male_mate_individual
            female_mate = mating_instance.female_mate_individual

            if mate in (male_mate, female_mate):
                return True

        return False

    def are_siblings(self, sibling) -> bool:
        """Check if two individuals are siblings.

        Accepts: Possible sibling of type Individual.
        Returns: Boolean result.
        """
        assert isinstance(sibling, Individual)

        condition1 = self.pedigree_identifier == sibling.pedigree_identifier
        condition2 = self.individual_father == sibling.individual_father
        condition3 = self.individual_mother == sibling.individual_mother

        if self.sibship_unit_relation is not None:
            assert isinstance(self.sibship_unit_relation, SibshipUnit)
            self_siblings = self.sibship_unit_relation.siblings_individuals
            condition_existence = sibling in self_siblings
            return condition1 and condition2 and condition3 and condition_existence

        return False

    def get_father_individual(self) -> Union[IndividualBase, None]:
        """Return the father of the individual like class object.

        Accepts: No arguments.
        Returns: Individual instance or None.
        """
        if self.mating_unit_relation is not None:
            assert isinstance(self.mating_unit_relation, MatingUnit)
            return self.mating_unit_relation.male_mate_individual
        return None

    def get_mother_individual(self) -> Union[IndividualBase, None]:
        """Return the mother of the individual like class object.

        Accepts: No arguments.
        Returns: Individual instance or None.
        """
        if self.mating_unit_relation is not None:
            assert isinstance(self.mating_unit_relation, MatingUnit)
            return self.mating_unit_relation.female_mate_individual
        return None


class MatingUnit(Generic[MatingUnitBase]):
    """Class Name: MatingUnit.

    This class is used to manage the
    base unit of a single mating unit
    in the structure of the pedigree.
    """

    __pedigree_identifier: str
    __male_mate_individual: Individual
    __female_mate_individual: Individual
    __sibship_unit_relation: Union[SibshipUnitBase, None]

    def __init__(self, pedigree_identifier,
                 male_mate_individual, female_mate_individual,
                 sibship_unit_relation=None) -> None:
        """Initialize an instance of the MatingUnit class.

        Parameters: The pedigree identifier of the pedigree,
        the male and the female mates (individuals) in the
        mating, the relation to the associated sibship.
        """
        try:
            assert isinstance(pedigree_identifier, str)
            assert isinstance(male_mate_individual, Individual)
            assert isinstance(female_mate_individual, Individual)
            assert isinstance(sibship_unit_relation, (SibshipUnit, type(None)))
        except AssertionError as assertion_error:
            message = 'The mating unit constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__pedigree_identifier = pedigree_identifier

        self.__male_mate_individual = male_mate_individual
        self.__female_mate_individual = female_mate_individual

        self.__sibship_unit_relation = sibship_unit_relation
        self.__generation_rank = None

    @property
    def pedigree_identifier(self) -> str:
        """Return the pedigree identifier property of the class."""
        return self.__pedigree_identifier

    @property
    def male_mate_individual(self) -> Individual:
        """Return the male mate individual property of the class."""
        return self.__male_mate_individual

    @property
    def female_mate_individual(self) -> Individual:
        """Return the female mate individual property of the class."""
        return self.__female_mate_individual

    @property
    def sibship_unit_relation(self) -> Union[SibshipUnitBase, None]:
        """Return the sibship unit relation property of the class."""
        return self.__sibship_unit_relation

    @property
    def generation_rank(self) -> Union[int, None]:
        """Return the generation rank property of the class."""
        return self.__generation_rank

    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation) -> None:
        assert isinstance(sibship_unit_relation, SibshipUnit)
        self.__sibship_unit_relation = sibship_unit_relation

    @generation_rank.setter
    def generation_rank(self, generation_rank) -> None:
        self.__generation_rank = generation_rank

    def __hash__(self) -> int:
        return hash(self.male_mate_individual) + \
                hash(self.female_mate_individual)

    def __eq__(self, mating_unit) -> bool:
        if not isinstance(mating_unit, MatingUnit):
            return False
        return self.__hash__() == mating_unit.__hash__()

    def __repr__(self) -> str:
        return "MU" + self.mating_string()

    def mating_string(self) -> str:
        """Return a unique string for the mating unit."""
        return '(' + str(self.male_mate_individual) + \
               ', ' + str(self.female_mate_individual) + ')'


class SibshipUnit(Generic[SibshipUnitBase]):
    """Class Name: SibshipUnit.

    This class is used to manage the
    base unit of a single sibship unit
    in the structure of the pedigree.
    """

    __pedigree_identifier: str
    __mating_unit_relation: Union[MatingUnitBase, None]

    def __init__(self, pedigree_identifier, mating_unit_relation=None) -> None:
        try:
            assert isinstance(pedigree_identifier,  str)
            assert isinstance(mating_unit_relation, (MatingUnit, type(None)))
        except AssertionError as assertion_error:
            message = 'The sibship unit constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__pedigree_identifier = pedigree_identifier

        self.__siblings_individuals = []
        self.__siblings_extended = []

        self.__mating_unit_relation = mating_unit_relation
        self.__generation_rank = None

    @property
    def pedigree_identifier(self) -> str:
        """Return the pedigree identifier property of the class."""
        return self.__pedigree_identifier

    @property
    def siblings_individuals(self) -> list:
        """Return the siblings individuals property of the class."""
        return self.__siblings_individuals

    @property
    def siblings_extended(self) -> list:
        """Return the siblings extended property of the class."""
        return self.__siblings_extended

    @property
    def mating_unit_relation(self) -> Union[MatingUnitBase, None]:
        """Return the mating unit relation property of the class."""
        return self.__mating_unit_relation

    @property
    def generation_rank(self) -> Union[int, None]:
        """Return the generation rank property of the class."""
        return self.__generation_rank

    @mating_unit_relation.setter
    def mating_unit_relation(self, mating_unit_relation) -> None:
        self.__mating_unit_relation = mating_unit_relation

    @generation_rank.setter
    def generation_rank(self, generation_rank) -> None:
        assert isinstance(generation_rank, int)
        self.__generation_rank = generation_rank

    def __hash__(self) -> int:
        return hash(self.mating_unit_relation)

    def __eq__(self, sibship_unit) -> bool:
        if not isinstance(sibship_unit, (SibshipUnit, type(None))):
            return False
        return self.__hash__() == sibship_unit.__hash__()

    def __repr__(self) -> str:
        return "SU" + self.mating_unit_relation.mating_string()

    def add_sibling_individual(self, sibling_individual) -> None:
        """Add an individual to the collection of siblings.
        The function accepts an instance of Individual class."""
        assert isinstance(sibling_individual, Individual)
        self.__siblings_individuals.append(sibling_individual)

    def add_sibling_individual_mate(self, sibling_individual_mate) -> None:
        """Add an individual mate to the collection of extended siblings.
        The function accepts an instance of Individual class."""
        assert isinstance(sibling_individual_mate, Individual)
        self.__siblings_extended.append(sibling_individual_mate)

    def change_sibling_individual(self, sibling_individual, index_child) -> None:
        """Change an individual from the collection of siblings.
        The function accepts an instance of Individual class
        and the index of the child - integer value."""
        assert isinstance(sibling_individual, Individual)
        assert isinstance(index_child, int)
        self.__siblings_individuals[index_child] = sibling_individual
