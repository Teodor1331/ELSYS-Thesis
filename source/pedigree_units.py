from pedigree_fields import Sex
from pedigree_fields import Status
from pedigree_fields import Role

from typing import Union
from typing import Optional


class Individual: pass
class MatingUnit: pass
class SibshipUnit: pass


class Individual:
    def __init__(self, individual_data) -> None:
        try:
            assert isinstance(individual_data, list)
        except AssertionError:
            raise AssertionError('The individual constructor arguments are not correct!')

        self.__pedigree_identifier      =   individual_data[0]
        self.__individual_identifier    =   individual_data[1]
        self.__individual_father        =   individual_data[2]
        self.__individual_mother        =   individual_data[3]

        self.__individual_sex           =   Individual.decide_sex_individual(individual_data[4])
        self.__individual_status        =   Individual.decide_status_individual(individual_data[5])
        self.__individual_role          =   Individual.decide_role_individual(individual_data[6])


        self.__mating_unit_relation     =   None
        self.__sibship_unit_relation    =   None

        self.__generation_rank          =   None
        self.__mating_instances         =   list()


    @property
    def pedigree_identifier(self) -> str:
        return self.__pedigree_identifier


    @property
    def individual_identifier(self) -> str:
        return self.__individual_identifier


    @property
    def individual_father(self) -> str:
        return self.__individual_father


    @property
    def individual_mother(self) -> str:
        return self.__individual_mother


    @property
    def individual_sex(self) -> Sex:
        return self.__individual_sex


    @property
    def individual_status(self) -> Status:
        return self.__individual_status


    @property
    def individual_role(self) -> Role:
        return self.__individual_role


    @property
    def mating_unit_relation(self) -> Union[MatingUnit, None]:
        return self.__mating_unit_relation


    @property
    def sibship_unit_relation(self) -> Union[SibshipUnit, None]:
        return self.__sibship_unit_relation


    @property
    def generation_rank(self) -> Union[int, None]:
        return self.__generation_rank


    @property
    def mating_instances(self):
        return self.__mating_instances


    @mating_unit_relation.setter
    def mating_unit_relation(self, mating_unit_relation):
        assert isinstance(mating_unit_relation, MatingUnit)
        self.__mating_unit_relation = mating_unit_relation


    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation):
        assert isinstance(sibship_unit_relation, SibshipUnit)
        self.__sibship_unit_relation = sibship_unit_relation


    @generation_rank.setter
    def generation_rank(self, generation_rank):
        assert isinstance(generation_rank, int)
        self.__generation_rank = generation_rank


    @mating_instances.setter
    def mating_instances(self, mating_instances):
        self.__mating_instances = mating_instances


    @pedigree_identifier.deleter
    def pedigree_identifier(self) -> None:
        del self.__pedigree_identifier


    @individual_identifier.deleter
    def individual_identifier(self) -> None:
        del self.__individual_identifier


    @individual_father.deleter
    def individual_father(self) -> None:
        del self.__individual_father


    @individual_mother.deleter
    def individual_mother(self) -> None:
        del self.__individual_mother


    @individual_sex.deleter
    def individual_sex(self) -> None:
        del self.__individual_sex


    @individual_status.deleter
    def individual_status(self) -> None:
        del self.__individual_status


    @individual_role.deleter
    def individual_role(self) -> None:
        del self.__individual_role


    @mating_unit_relation.deleter
    def mating_unit_relation(self) -> None:
        del self.__mating_unit_relation


    @sibship_unit_relation.deleter
    def sibship_unit_relation(self) -> None:
        del self.__sibship_unit_relation


    @generation_rank.deleter
    def generation_rank(self) -> None:
        del self.__generation_rank


    @mating_instances.deleter
    def mating_instances(self) -> None:
        del self.__mating_instances


    def __hash__(self) -> int:
        return  hash(self.pedigree_identifier) + \
                hash(self.individual_identifier)


    def __eq__(self, individual) -> bool:
        if not isinstance(individual, Individual):
            return False
        return  self.__hash__() == individual.__hash__()


    def __repr__(self) -> str:
        return self.individual_identifier


    def __del__(self) -> None:
        del self.__pedigree_identifier
        del self.__individual_identifier
        del self.__individual_father
        del self.__individual_mother

        del self.__individual_sex
        del self.__individual_status
        del self.__individual_role

        del self.__mating_unit_relation
        del self.__sibship_unit_relation

        del self.__generation_rank
        del self.__mating_instances


    @staticmethod
    def decide_sex_individual(string) -> Sex:
        try:
            assert isinstance(string, str)
        except AssertionError:
            raise AssertionError('The given argument is not a string!')

        if string == '1':
            return Sex.MALE
        elif string == '2':
            return Sex.FEMALE
        else:
            return Sex.UNKNOWN


    @staticmethod
    def decide_status_individual(string) -> Status:
        try:
            assert isinstance(string, str)
        except AssertionError:
            raise AssertionError('The given argument is not a string!')

        if string == '1':
            return Status.UNAFFECTED
        elif string == '2':
            return Status.AFFECTED
        else:
            return Status.UNKNOWN


    @staticmethod
    def decide_role_individual(string) -> Role:
        try:
            assert isinstance(string, str)
        except AssertionError:
            raise AssertionError('The given argument is not a string!')

        if string == 'prb':
            return Role.PROBAND
        elif string == 'father':
            return Role.FATHER
        elif string == 'mother':
            return Role.MOTHER
        elif string == 'brother':
            return Role.BROTHER
        elif string == 'sister':
            return Role.SISTER
        elif string == 'grandfather':
            return Role.GRANDFATHER
        elif string == 'grandmother':
            return Role.GRANDMOTHER
        else:
            return Role.UNKNOWN


class MatingUnit:
    def __init__(self, pedigree_identifier, male_mate_individual, female_mate_individual, sibship_unit_relation = None) -> None:
        try:
            assert isinstance(pedigree_identifier, str)
            assert isinstance(male_mate_individual, Individual)
            assert isinstance(female_mate_individual, Individual)
            assert isinstance(sibship_unit_relation, (SibshipUnit, type(None)))
        except AssertionError:
            raise AssertionError('The mating unit constructor arguments are not correct!')

        self.__pedigree_identifier      =   pedigree_identifier

        self.__male_mate_individual     =   male_mate_individual
        self.__female_mate_individual   =   female_mate_individual

        self.__sibship_unit_relation    =   sibship_unit_relation
        self.__generation_rank          =   None


    @property
    def pedigree_identifier(self) -> str:
        return self.__pedigree_identifier


    @property
    def male_mate_individual(self) -> Individual:
        return self.__male_mate_individual


    @property
    def female_mate_individual(self) -> Individual:
        return self.__female_mate_individual


    @property
    def sibship_unit_relation(self) -> Union[SibshipUnit, None]:
        return self.__sibship_unit_relation


    @property
    def generation_rank(self) -> Union[int, None]:
        return self.__generation_rank


    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation):
        assert isinstance(sibship_unit_relation, SibshipUnit)
        self.__sibship_unit_relation = sibship_unit_relation


    @generation_rank.setter
    def generation_rank(self, generation_rank):
        self.__generation_rank = generation_rank


    @pedigree_identifier.deleter
    def pedigree_identifier(self):
        del self.__pedigree_identifier


    @male_mate_individual.deleter
    def male_mate_individual(self):
        del self.__male_mate_individual


    @female_mate_individual.deleter
    def female_mate_individual(self):
        del self.__female_mate_individual


    @sibship_unit_relation.deleter
    def sibship_unit_relation(self):
        del self.__sibship_unit_relation


    @generation_rank.deleter
    def generation_rank(self):
        del self.__generation_rank


    def __hash__(self) -> int:
        return  hash(self.male_mate_individual) + \
                hash(self.female_mate_individual)


    def __eq__(self, mating_unit) -> bool:
        if not isinstance(mating_unit, MatingUnit):
            return False
        return self.__hash__() == mating_unit.__hash__()


    def __repr__(self) -> str:
        return "MU" + self.mating_string()


    def __del__(self):
        del self.__pedigree_identifier

        del self.__male_mate_individual
        del self.__female_mate_individual

        del self.__sibship_unit_relation
        del self.__generation_rank


    def mating_string(self) -> str:
        return  '(' + str(self.male_mate_individual) + \
                ', ' + str(self.female_mate_individual) + ')'


class SibshipUnit:
    def __init__(self, pedigree_identifier, mating_unit_relation = None) -> None:
        try:
            assert isinstance(pedigree_identifier,  str)
            assert isinstance(mating_unit_relation, (MatingUnit, type(None)))
        except AssertionError:
            raise AssertionError('The sibship unit constructor arguments are not correct!')

        self.__pedigree_identifier      =   pedigree_identifier

        self.__siblings_individuals     =   []
        self.__siblings_extended        =   []

        self.__mating_unit_relation     =   mating_unit_relation
        self.__generation_rank          =   None


    @property
    def pedigree_identifier(self) -> str:
        return self.__pedigree_identifier


    @property
    def siblings_individuals(self) -> list:
        return self.__siblings_individuals


    @property
    def siblings_extended(self) -> list:
        return self.__siblings_extended


    @property
    def mating_unit_relation(self):
        return self.__mating_unit_relation


    @property
    def generation_rank(self):
        return self.__generation_rank


    @siblings_individuals.setter
    def siblings_individuals(self, siblings_individuals):
        self.__siblings_individuals = siblings_individuals


    @siblings_extended.setter
    def siblings_extended(self, siblings_extended):
        self.__siblings_extended = siblings_extended


    @mating_unit_relation.setter
    def mating_unit_relation(self, mating_unit_relation):
        self.__mating_unit_relation = mating_unit_relation


    @generation_rank.setter
    def generation_rank(self, generation_rank):
        assert isinstance(generation_rank, int)
        self.__generation_rank = generation_rank


    @pedigree_identifier.deleter
    def pedigree_identifier(self) -> None:
        del self.__pedigree_identifier


    @siblings_individuals.deleter
    def siblings_individuals(self) -> None:
        del self.__siblings_individuals


    @siblings_extended.deleter
    def siblings_extended(self) -> None:
        del self.__siblings_extended


    @mating_unit_relation.deleter
    def mating_unit_relation(self):
        del self.__mating_unit_relation


    @generation_rank.deleter
    def generation_rank(self):
        del self.__generation_rank


    def __hash__(self):
        return hash(self.mating_unit_relation)


    def __eq__(self, sibship_unit):
        if not isinstance(sibship_unit, (SibshipUnit, type(None))):
            return False
        return self.__hash__() == sibship_unit.__hash__()


    def __repr__(self):
        return "SU" + self.mating_unit_relation.mating_string()


    def __del__(self) -> None:
        del self.__pedigree_identifier
        del self.__siblings_individuals
        del self.__siblings_extended
        del self.__mating_unit_relation
        del self.__generation_rank


    def add_sibling_individual(self, sibling_individual):
        assert isinstance(sibling_individual, Individual)
        self.__siblings_individuals.append(sibling_individual)


    def add_sibling_individual_mate(self, sibling_individual_mate):
        assert isinstance(sibling_individual_mate, Individual)
        self.__siblings_extended.append(sibling_individual_mate)


    def change_sibling_individual(self, sibling_individual, index_child):
        assert isinstance(sibling_individual, Individual)
        assert isinstance(index_child, int)
        self.__siblings_individuals[index_child] = sibling_individual
