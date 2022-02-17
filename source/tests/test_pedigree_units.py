import sys, pytest
sys.path.append('..')

from pedigree_units import Individual
from pedigree_units import MatingUnit
from pedigree_units import SibshipUnit
from pedigree_fields import Sex, Status, Role


def test_individual_constructor():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'null'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'null'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'null'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'null'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'null'])

    assert isinstance(individual1, Individual)
    assert isinstance(individual2, Individual)
    assert isinstance(individual3, Individual)
    assert isinstance(individual4, Individual)
    assert isinstance(individual5, Individual)
    assert isinstance(individual6, Individual)

    assert 'individual1' in locals()
    assert 'individual2' in locals()
    assert 'individual3' in locals()
    assert 'individual4' in locals()
    assert 'individual5' in locals()

    assert locals()['individual1'] is individual1
    assert locals()['individual2'] is individual2
    assert locals()['individual3'] is individual3
    assert locals()['individual4'] is individual4
    assert locals()['individual5'] is individual5
    assert locals()['individual6'] is individual6

    with pytest.raises(AssertionError):
        Individual(None), Individual(bool)
        Individual(int), Individual(float), Individual(complex)
        Individual(bytes), Individual(bytearray), Individual(str)
        Individual(tuple), Individual(range)
        Individual(set), Individual(frozenset), Individual(dict)


def test_individual_destructor():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'null'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'null'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'null'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'null'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'null'])

    del individual1
    del individual2
    del individual3
    del individual4
    del individual5
    del individual6

    assert 'individual1' not in locals()
    assert 'individual2' not in locals()
    assert 'individual3' not in locals()
    assert 'individual4' not in locals()
    assert 'individual5' not in locals()
    assert 'individual6' not in locals()


def test_individual_properties():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'father'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'mother'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'prb'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'brother'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'sister'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'sister'])

    assert hasattr(individual1, 'pedigree_identifier')
    assert hasattr(individual2, 'pedigree_identifier')
    assert hasattr(individual3, 'pedigree_identifier')
    assert hasattr(individual4, 'pedigree_identifier')
    assert hasattr(individual5, 'pedigree_identifier')
    assert hasattr(individual6, 'pedigree_identifier')

    assert hasattr(individual1, 'individual_identifier')
    assert hasattr(individual2, 'individual_identifier')
    assert hasattr(individual3, 'individual_identifier')
    assert hasattr(individual4, 'individual_identifier')
    assert hasattr(individual5, 'individual_identifier')
    assert hasattr(individual6, 'individual_identifier')

    assert hasattr(individual1, 'individual_father')
    assert hasattr(individual2, 'individual_father')
    assert hasattr(individual3, 'individual_father')
    assert hasattr(individual4, 'individual_father')
    assert hasattr(individual5, 'individual_father')
    assert hasattr(individual6, 'individual_father')
    
    assert hasattr(individual1, 'individual_mother')
    assert hasattr(individual2, 'individual_mother')
    assert hasattr(individual3, 'individual_mother')
    assert hasattr(individual4, 'individual_mother')
    assert hasattr(individual5, 'individual_mother')
    assert hasattr(individual6, 'individual_mother')

    assert hasattr(individual1, 'individual_sex')
    assert hasattr(individual2, 'individual_sex')
    assert hasattr(individual3, 'individual_sex')
    assert hasattr(individual4, 'individual_sex')
    assert hasattr(individual5, 'individual_sex')
    assert hasattr(individual6, 'individual_sex')

    assert hasattr(individual1, 'individual_status')
    assert hasattr(individual2, 'individual_status')
    assert hasattr(individual3, 'individual_status')
    assert hasattr(individual4, 'individual_status')
    assert hasattr(individual5, 'individual_status')
    assert hasattr(individual6, 'individual_status')

    assert hasattr(individual1, 'individual_role')
    assert hasattr(individual2, 'individual_role')
    assert hasattr(individual3, 'individual_role')
    assert hasattr(individual4, 'individual_role')
    assert hasattr(individual5, 'individual_role')
    assert hasattr(individual6, 'individual_role')

    assert hasattr(individual1, 'mating_unit_relation')
    assert hasattr(individual2, 'mating_unit_relation')
    assert hasattr(individual3, 'mating_unit_relation')
    assert hasattr(individual4, 'mating_unit_relation')
    assert hasattr(individual5, 'mating_unit_relation')
    assert hasattr(individual6, 'mating_unit_relation')

    assert hasattr(individual1, 'sibship_unit_relation')
    assert hasattr(individual2, 'sibship_unit_relation')
    assert hasattr(individual3, 'sibship_unit_relation')
    assert hasattr(individual4, 'sibship_unit_relation')
    assert hasattr(individual5, 'sibship_unit_relation')
    assert hasattr(individual6, 'sibship_unit_relation')

    assert hasattr(individual1, 'generation_rank')
    assert hasattr(individual2, 'generation_rank')
    assert hasattr(individual3, 'generation_rank')
    assert hasattr(individual4, 'generation_rank')
    assert hasattr(individual5, 'generation_rank')
    assert hasattr(individual6, 'generation_rank')

    assert hasattr(individual1, 'mating_instances')
    assert hasattr(individual2, 'mating_instances')
    assert hasattr(individual3, 'mating_instances')
    assert hasattr(individual4, 'mating_instances')
    assert hasattr(individual5, 'mating_instances')
    assert hasattr(individual6, 'mating_instances')

    assert isinstance(individual1.pedigree_identifier, str)
    assert isinstance(individual2.pedigree_identifier, str)
    assert isinstance(individual3.pedigree_identifier, str)
    assert isinstance(individual4.pedigree_identifier, str)
    assert isinstance(individual5.pedigree_identifier, str)
    assert isinstance(individual6.pedigree_identifier, str)

    assert isinstance(individual1.individual_identifier, str)
    assert isinstance(individual2.individual_identifier, str)
    assert isinstance(individual3.individual_identifier, str)
    assert isinstance(individual4.individual_identifier, str)
    assert isinstance(individual5.individual_identifier, str)
    assert isinstance(individual6.individual_identifier, str)

    assert isinstance(individual1.individual_father, str)
    assert isinstance(individual2.individual_father, str)
    assert isinstance(individual3.individual_father, str)
    assert isinstance(individual4.individual_father, str)
    assert isinstance(individual5.individual_father, str)
    assert isinstance(individual6.individual_father, str)

    assert isinstance(individual1.individual_mother, str)
    assert isinstance(individual2.individual_mother, str)
    assert isinstance(individual3.individual_mother, str)
    assert isinstance(individual4.individual_mother, str)
    assert isinstance(individual5.individual_mother, str)
    assert isinstance(individual6.individual_mother, str)

    assert isinstance(individual1.individual_sex, Sex)
    assert isinstance(individual2.individual_sex, Sex)
    assert isinstance(individual3.individual_sex, Sex)
    assert isinstance(individual4.individual_sex, Sex)
    assert isinstance(individual5.individual_sex, Sex)
    assert isinstance(individual6.individual_sex, Sex)

    assert isinstance(individual1.individual_status, Status)
    assert isinstance(individual2.individual_status, Status)
    assert isinstance(individual3.individual_status, Status)
    assert isinstance(individual4.individual_status, Status)
    assert isinstance(individual5.individual_status, Status)
    assert isinstance(individual6.individual_status, Status)

    assert isinstance(individual1.individual_role, Role)
    assert isinstance(individual2.individual_role, Role)
    assert isinstance(individual3.individual_role, Role)
    assert isinstance(individual4.individual_role, Role)
    assert isinstance(individual5.individual_role, Role)
    assert isinstance(individual6.individual_role, Role)

    assert isinstance(individual1.mating_unit_relation, (MatingUnit, type(None)))
    assert isinstance(individual2.mating_unit_relation, (MatingUnit, type(None)))
    assert isinstance(individual3.mating_unit_relation, (MatingUnit, type(None)))
    assert isinstance(individual4.mating_unit_relation, (MatingUnit, type(None)))
    assert isinstance(individual5.mating_unit_relation, (MatingUnit, type(None)))
    assert isinstance(individual6.mating_unit_relation, (MatingUnit, type(None)))

    assert isinstance(individual1.sibship_unit_relation, (SibshipUnit, type(None)))
    assert isinstance(individual2.sibship_unit_relation, (SibshipUnit, type(None)))
    assert isinstance(individual3.sibship_unit_relation, (SibshipUnit, type(None)))
    assert isinstance(individual4.sibship_unit_relation, (SibshipUnit, type(None)))
    assert isinstance(individual5.sibship_unit_relation, (SibshipUnit, type(None)))
    assert isinstance(individual6.sibship_unit_relation, (SibshipUnit, type(None)))

    assert isinstance(individual1.generation_rank, (int, type(None)))
    assert isinstance(individual2.generation_rank, (int, type(None)))
    assert isinstance(individual3.generation_rank, (int, type(None)))
    assert isinstance(individual4.generation_rank, (int, type(None)))
    assert isinstance(individual5.generation_rank, (int, type(None)))

    assert isinstance(individual1.mating_instances, list)
    assert isinstance(individual2.mating_instances, list)
    assert isinstance(individual3.mating_instances, list)
    assert isinstance(individual4.mating_instances, list)
    assert isinstance(individual5.mating_instances, list)
    assert isinstance(individual6.mating_instances, list)

    assert individual1.pedigree_identifier == 'ped'
    assert individual2.pedigree_identifier == 'ped'
    assert individual3.pedigree_identifier == 'ped'
    assert individual4.pedigree_identifier == 'ped'
    assert individual5.pedigree_identifier == 'ped'
    assert individual6.pedigree_identifier == 'ped'

    assert individual1.individual_identifier == 'father'
    assert individual2.individual_identifier == 'mother'
    assert individual3.individual_identifier == 'son1'
    assert individual4.individual_identifier == 'son2'
    assert individual5.individual_identifier == 'dau1'
    assert individual6.individual_identifier == 'dau2'

    assert individual1.individual_father == '0'
    assert individual2.individual_father == '0'
    assert individual3.individual_father == 'father'
    assert individual4.individual_father == 'father'
    assert individual5.individual_father == 'father'
    assert individual6.individual_father == 'father'

    assert individual1.individual_mother == '0'
    assert individual2.individual_mother == '0'
    assert individual3.individual_mother == 'mother'
    assert individual4.individual_mother == 'mother'
    assert individual5.individual_mother == 'mother'
    assert individual6.individual_mother == 'mother'

    assert individual1.individual_sex == Sex.MALE
    assert individual2.individual_sex == Sex.FEMALE
    assert individual3.individual_sex == Sex.MALE
    assert individual4.individual_sex == Sex.MALE
    assert individual5.individual_sex == Sex.FEMALE
    assert individual6.individual_sex == Sex.FEMALE

    assert individual1.individual_status == Status.AFFECTED
    assert individual2.individual_status == Status.UNAFFECTED
    assert individual3.individual_status == Status.AFFECTED
    assert individual4.individual_status == Status.UNAFFECTED
    assert individual5.individual_status == Status.AFFECTED
    assert individual6.individual_status == Status.UNAFFECTED

    assert individual1.individual_role == Role.FATHER
    assert individual2.individual_role == Role.MOTHER
    assert individual3.individual_role == Role.PROBAND
    assert individual4.individual_role == Role.BROTHER
    assert individual5.individual_role == Role.SISTER
    assert individual6.individual_role == Role.SISTER

    assert individual1.mating_unit_relation is None
    assert individual2.mating_unit_relation is None
    assert individual3.mating_unit_relation is None
    assert individual4.mating_unit_relation is None
    assert individual5.mating_unit_relation is None
    assert individual6.mating_unit_relation is None

    assert individual1.sibship_unit_relation is None
    assert individual2.sibship_unit_relation is None
    assert individual3.sibship_unit_relation is None
    assert individual4.sibship_unit_relation is None
    assert individual5.sibship_unit_relation is None
    assert individual6.sibship_unit_relation is None

    assert individual1.generation_rank is None
    assert individual2.generation_rank is None
    assert individual3.generation_rank is None
    assert individual4.generation_rank is None
    assert individual5.generation_rank is None
    assert individual6.generation_rank is None

    assert individual1.mating_instances == list()
    assert individual2.mating_instances == list()
    assert individual3.mating_instances == list()
    assert individual4.mating_instances == list()
    assert individual5.mating_instances == list()
    assert individual6.mating_instances == list()

    assert len(individual1.mating_instances) == 0
    assert len(individual2.mating_instances) == 0
    assert len(individual3.mating_instances) == 0
    assert len(individual4.mating_instances) == 0
    assert len(individual5.mating_instances) == 0
    assert len(individual6.mating_instances) == 0


def test_individual_deleters():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'father'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'mother'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'prb'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'brother'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'sister'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'sister'])

    del individual1.pedigree_identifier
    del individual2.pedigree_identifier
    del individual3.pedigree_identifier
    del individual4.pedigree_identifier
    del individual5.pedigree_identifier
    del individual6.pedigree_identifier

    del individual1.individual_identifier
    del individual2.individual_identifier
    del individual3.individual_identifier
    del individual4.individual_identifier
    del individual5.individual_identifier
    del individual6.individual_identifier

    del individual1.individual_father
    del individual2.individual_father
    del individual3.individual_father
    del individual4.individual_father
    del individual5.individual_father
    del individual6.individual_father

    del individual1.individual_mother
    del individual2.individual_mother
    del individual3.individual_mother
    del individual4.individual_mother
    del individual5.individual_mother
    del individual6.individual_mother

    del individual1.individual_sex
    del individual2.individual_sex
    del individual3.individual_sex
    del individual4.individual_sex
    del individual5.individual_sex
    del individual6.individual_sex

    del individual1.individual_status
    del individual2.individual_status
    del individual3.individual_status
    del individual4.individual_status
    del individual5.individual_status
    del individual6.individual_status

    del individual1.individual_role
    del individual2.individual_role
    del individual3.individual_role
    del individual4.individual_role
    del individual5.individual_role
    del individual6.individual_role

    del individual1.mating_unit_relation
    del individual2.mating_unit_relation
    del individual3.mating_unit_relation
    del individual4.mating_unit_relation
    del individual5.mating_unit_relation
    del individual6.mating_unit_relation

    del individual1.sibship_unit_relation
    del individual2.sibship_unit_relation
    del individual3.sibship_unit_relation
    del individual4.sibship_unit_relation
    del individual5.sibship_unit_relation
    del individual6.sibship_unit_relation

    del individual1.generation_rank
    del individual2.generation_rank
    del individual3.generation_rank
    del individual4.generation_rank
    del individual5.generation_rank
    del individual6.generation_rank

    del individual1.mating_instances
    del individual2.mating_instances
    del individual3.mating_instances
    del individual4.mating_instances
    del individual5.mating_instances
    del individual6.mating_instances

    assert not hasattr(individual1, 'pedigree_identifier')
    assert not hasattr(individual2, 'pedigree_identifier')
    assert not hasattr(individual3, 'pedigree_identifier')
    assert not hasattr(individual4, 'pedigree_identifier')
    assert not hasattr(individual5, 'pedigree_identifier')
    assert not hasattr(individual6, 'pedigree_identifier')

    assert not hasattr(individual1, 'individual_identifier')
    assert not hasattr(individual2, 'individual_identifier')
    assert not hasattr(individual3, 'individual_identifier')
    assert not hasattr(individual4, 'individual_identifier')
    assert not hasattr(individual5, 'individual_identifier')
    assert not hasattr(individual6, 'individual_identifier')

    assert not hasattr(individual1, 'individual_father')
    assert not hasattr(individual2, 'individual_father')
    assert not hasattr(individual3, 'individual_father')
    assert not hasattr(individual4, 'individual_father')
    assert not hasattr(individual5, 'individual_father')
    assert not hasattr(individual6, 'individual_father')

    assert not hasattr(individual1, 'individual_mother')
    assert not hasattr(individual2, 'individual_mother')
    assert not hasattr(individual3, 'individual_mother')
    assert not hasattr(individual4, 'individual_mother')
    assert not hasattr(individual5, 'individual_mother')
    assert not hasattr(individual6, 'individual_mother')

    assert not hasattr(individual1, 'individual_sex')
    assert not hasattr(individual2, 'individual_sex')
    assert not hasattr(individual3, 'individual_sex')
    assert not hasattr(individual4, 'individual_sex')
    assert not hasattr(individual5, 'individual_sex')
    assert not hasattr(individual6, 'individual_sex')

    assert not hasattr(individual1, 'individual_status')
    assert not hasattr(individual2, 'individual_status')
    assert not hasattr(individual3, 'individual_status')
    assert not hasattr(individual4, 'individual_status')
    assert not hasattr(individual5, 'individual_status')
    assert not hasattr(individual6, 'individual_status')

    assert not hasattr(individual1, 'individual_role')
    assert not hasattr(individual2, 'individual_role')
    assert not hasattr(individual3, 'individual_role')
    assert not hasattr(individual4, 'individual_role')
    assert not hasattr(individual5, 'individual_role')
    assert not hasattr(individual6, 'individual_role')

    assert not hasattr(individual1, 'mating_unit_relation')
    assert not hasattr(individual2, 'mating_unit_relation')
    assert not hasattr(individual3, 'mating_unit_relation')
    assert not hasattr(individual4, 'mating_unit_relation')
    assert not hasattr(individual5, 'mating_unit_relation')
    assert not hasattr(individual6, 'mating_unit_relation')

    assert not hasattr(individual1, 'sibship_unit_relation')
    assert not hasattr(individual2, 'sibship_unit_relation')
    assert not hasattr(individual3, 'sibship_unit_relation')
    assert not hasattr(individual4, 'sibship_unit_relation')
    assert not hasattr(individual5, 'sibship_unit_relation')
    assert not hasattr(individual6, 'sibship_unit_relation')


def test_individual_hash_code_method():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'father'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'mother'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'prb'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'brother'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'sister'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'sister'])

    assert isinstance(individual1.__hash__(), int)
    assert isinstance(individual2.__hash__(), int)
    assert isinstance(individual3.__hash__(), int)
    assert isinstance(individual4.__hash__(), int)
    assert isinstance(individual5.__hash__(), int)
    assert isinstance(individual6.__hash__(), int)

    assert individual1.__hash__() == hash(individual1.pedigree_identifier) + hash(individual1.individual_identifier)
    assert individual2.__hash__() == hash(individual2.pedigree_identifier) + hash(individual2.individual_identifier)
    assert individual3.__hash__() == hash(individual3.pedigree_identifier) + hash(individual3.individual_identifier)
    assert individual4.__hash__() == hash(individual4.pedigree_identifier) + hash(individual4.individual_identifier)
    assert individual5.__hash__() == hash(individual5.pedigree_identifier) + hash(individual5.individual_identifier)
    assert individual6.__hash__() == hash(individual6.pedigree_identifier) + hash(individual6.individual_identifier)


def test_individual_equals_method():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'father'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'mother'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'prb'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'brother'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'sister'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'sister'])

    assert isinstance(individual1.__eq__(None), bool)
    assert isinstance(individual2.__eq__(None), bool)
    assert isinstance(individual3.__eq__(None), bool)
    assert isinstance(individual4.__eq__(None), bool)
    assert isinstance(individual5.__eq__(None), bool)
    assert isinstance(individual6.__eq__(None), bool)

    assert (individual1 == None) is False
    assert (individual2 == None) is False
    assert (individual3 == None) is False
    assert (individual4 == None) is False
    assert (individual5 == None) is False
    assert (individual6 == None) is False

    assert (individual1 == bool) is False
    assert (individual2 == bool) is False
    assert (individual3 == bool) is False
    assert (individual4 == bool) is False
    assert (individual5 == bool) is False
    assert (individual6 == bool) is False

    assert (individual1 == int) is False
    assert (individual2 == int) is False
    assert (individual3 == int) is False
    assert (individual4 == int) is False
    assert (individual5 == int) is False
    assert (individual6 == int) is False

    assert (individual1 == float) is False
    assert (individual2 == float) is False
    assert (individual3 == float) is False
    assert (individual4 == float) is False
    assert (individual5 == float) is False
    assert (individual6 == float) is False

    assert (individual1 == complex) is False
    assert (individual2 == complex) is False
    assert (individual3 == complex) is False
    assert (individual4 == complex) is False
    assert (individual5 == complex) is False
    assert (individual6 == complex) is False

    assert (individual1 == str) is False
    assert (individual2 == str) is False
    assert (individual3 == str) is False
    assert (individual4 == str) is False
    assert (individual5 == str) is False
    assert (individual6 == str) is False

    assert (individual1 == individual4) is False
    assert (individual2 == individual5) is False
    assert (individual3 == individual6) is False
    assert (individual4 == individual1) is False
    assert (individual5 == individual2) is False
    assert (individual6 == individual3) is False
    
    assert (individual1 == individual1) is True
    assert (individual2 == individual2) is True
    assert (individual3 == individual3) is True
    assert (individual4 == individual4) is True
    assert (individual5 == individual5) is True
    assert (individual6 == individual6) is True


def test_individual_string_representation_method():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'father'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'mother'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'prb'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'brother'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'sister'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'sister'])

    assert isinstance(individual1.__repr__(), str)
    assert isinstance(individual2.__repr__(), str)
    assert isinstance(individual3.__repr__(), str)
    assert isinstance(individual4.__repr__(), str)
    assert isinstance(individual5.__repr__(), str)
    assert isinstance(individual6.__repr__(), str)

    assert str(individual1) == repr(individual1) == 'father'
    assert str(individual2) == repr(individual2) == 'mother'
    assert str(individual3) == repr(individual3) == 'son1'
    assert str(individual4) == repr(individual4) == 'son2'
    assert str(individual5) == repr(individual5) == 'dau1'
    assert str(individual6) == repr(individual6) == 'dau2'


def test_individual_decide_enumerations_methods():
    assert isinstance(Individual.decide_sex_individual('String'), Sex)
    assert isinstance(Individual.decide_status_individual('String'), Status)
    assert isinstance(Individual.decide_role_individual('String'), Role)

    assert Individual.decide_sex_individual('0') == Sex.UNKNOWN
    assert Individual.decide_sex_individual('1') == Sex.MALE
    assert Individual.decide_sex_individual('2') == Sex.FEMALE

    assert Individual.decide_status_individual('0') == Status.UNKNOWN
    assert Individual.decide_status_individual('1') == Status.UNAFFECTED
    assert Individual.decide_status_individual('2') == Status.AFFECTED

    assert Individual.decide_role_individual('prb') == Role.PROBAND
    assert Individual.decide_role_individual('father') == Role.FATHER
    assert Individual.decide_role_individual('mother') == Role.MOTHER
    assert Individual.decide_role_individual('brother') == Role.BROTHER
    assert Individual.decide_role_individual('sister') == Role.SISTER
    assert Individual.decide_role_individual('grandfather') == Role.GRANDFATHER
    assert Individual.decide_role_individual('grandmother') == Role.GRANDMOTHER
    assert Individual.decide_role_individual('null') == Role.UNKNOWN

    with pytest.raises(AssertionError):
        Individual.decide_sex_individual(None)
        Individual.decide_sex_individual(int)
        Individual.decide_sex_individual(float)
        Individual.decide_sex_individual(bool)

        Individual.decide_status_individual(None)
        Individual.decide_status_individual(int)
        Individual.decide_status_individual(float)
        Individual.decide_status_individual(bool)

        Individual.decide_role_individual(None)
        Individual.decide_role_individual(int)
        Individual.decide_role_individual(float)
        Individual.decide_role_individual(bool) 


def test_mating_unit_constructor():
    individual1 = Individual(['pedigree', 'male_mate1', '0', '0', '1', '0', 'null'])
    individual2 = Individual(['pedigree', 'male_mate2', '0', '0', '1', '0', 'null'])
    individual3 = Individual(['pedigree', 'male_mate3', '0', '0', '1', '0', 'null'])
    individual4 = Individual(['pedigree', 'female_mate1', '0', '0', '2', '0', 'null'])
    individual5 = Individual(['pedigree', 'female_mate2', '0', '0', '2', '0', 'null'])
    individual6 = Individual(['pedigree', 'female_mate3', '0', '0', '2', '0', 'null'])

    mating_unit1 = MatingUnit('pedigree', individual1, individual4)
    mating_unit2 = MatingUnit('pedigree', individual2, individual5)
    mating_unit3 = MatingUnit('pedigree', individual3, individual6)

    assert isinstance(mating_unit1, MatingUnit)
    assert isinstance(mating_unit2, MatingUnit)
    assert isinstance(mating_unit3, MatingUnit)

    assert 'mating_unit1' in locals()
    assert 'mating_unit2' in locals()
    assert 'mating_unit3' in locals()

    assert locals()['mating_unit1'] is mating_unit1
    assert locals()['mating_unit2'] is mating_unit2
    assert locals()['mating_unit3'] is mating_unit3

    with pytest.raises(AssertionError):
        MatingUnit(None, individual1, individual4)
        MatingUnit(bool, individual1, individual4)
        MatingUnit(int, individual1, individual4)
        MatingUnit(float, individual1, individual4)
        MatingUnit(complex, individual1, individual4)

        MatingUnit('pedigree', None, individual5)
        MatingUnit('pedigree', bool, individual5)
        MatingUnit('pedigree', int, individual5)
        MatingUnit('pedigree', float, individual5)
        MatingUnit('pedigree', complex, individual5)
        MatingUnit('pedigree', str, individual5)

        MatingUnit('pedigree', individual2, None)
        MatingUnit('pedigree', individual2, bool)
        MatingUnit('pedigree', individual2, int)
        MatingUnit('pedigree', individual2, float)
        MatingUnit('pedigree', individual2, complex)
        MatingUnit('pedigree', individual2, str)

        MatingUnit('pedigree', individual3, individual6, bool)
        MatingUnit('pedigree', individual3, individual6, int)
        MatingUnit('pedigree', individual3, individual6, float)
        MatingUnit('pedigree', individual3, individual6, complex)
        MatingUnit('pedigree', individual3, individual6, str)


def test_mating_unit_properties():
    individual1 = Individual(['ped', 'male_mate1', '0', '0', '1', '0', 'null'])
    individual2 = Individual(['ped', 'male_mate2', '0', '0', '1', '0', 'null'])
    individual3 = Individual(['ped', 'male_mate3', '0', '0', '1', '0', 'null'])
    individual4 = Individual(['ped', 'female_mate1', '0', '0', '2', '0', 'null'])
    individual5 = Individual(['ped', 'female_mate2', '0', '0', '2', '0', 'null'])
    individual6 = Individual(['ped', 'female_mate3', '0', '0', '2', '0', 'null'])

    mating_unit1 = MatingUnit('ped', individual1, individual4)
    mating_unit2 = MatingUnit('ped', individual2, individual5)
    mating_unit3 = MatingUnit('ped', individual3, individual6)

    assert hasattr(mating_unit1, 'pedigree_identifier')
    assert hasattr(mating_unit2, 'pedigree_identifier')
    assert hasattr(mating_unit3, 'pedigree_identifier')

    assert hasattr(mating_unit1, 'male_mate_individual')
    assert hasattr(mating_unit2, 'male_mate_individual')
    assert hasattr(mating_unit3, 'male_mate_individual')

    assert hasattr(mating_unit1, 'female_mate_individual')
    assert hasattr(mating_unit2, 'female_mate_individual')
    assert hasattr(mating_unit3, 'female_mate_individual')

    assert hasattr(mating_unit1, 'sibship_unit_relation')
    assert hasattr(mating_unit2, 'sibship_unit_relation')
    assert hasattr(mating_unit3, 'sibship_unit_relation')
    
    assert hasattr(mating_unit1, 'generation_rank')
    assert hasattr(mating_unit2, 'generation_rank')
    assert hasattr(mating_unit3, 'generation_rank')

    assert isinstance(mating_unit1.pedigree_identifier, str)
    assert isinstance(mating_unit2.pedigree_identifier, str)
    assert isinstance(mating_unit3.pedigree_identifier, str)

    assert isinstance(mating_unit1.male_mate_individual, Individual)
    assert isinstance(mating_unit2.male_mate_individual, Individual)
    assert isinstance(mating_unit3.male_mate_individual, Individual)

    assert isinstance(mating_unit1.female_mate_individual, Individual)
    assert isinstance(mating_unit2.female_mate_individual, Individual)
    assert isinstance(mating_unit3.female_mate_individual, Individual)

    assert isinstance(mating_unit1.sibship_unit_relation, (SibshipUnit, type(None)))
    assert isinstance(mating_unit2.sibship_unit_relation, (SibshipUnit, type(None)))
    assert isinstance(mating_unit3.sibship_unit_relation, (SibshipUnit, type(None)))

    assert isinstance(mating_unit1.generation_rank, (int, type(None)))
    assert isinstance(mating_unit2.generation_rank, (int, type(None)))
    assert isinstance(mating_unit3.generation_rank, (int, type(None)))

    assert mating_unit1.pedigree_identifier == 'ped'
    assert mating_unit2.pedigree_identifier == 'ped'
    assert mating_unit3.pedigree_identifier == 'ped'

    assert mating_unit1.male_mate_individual == Individual(['ped', 'male_mate1', '0', '0', '1', '0', 'null'])
    assert mating_unit2.male_mate_individual == Individual(['ped', 'male_mate2', '0', '0', '1', '0', 'null'])
    assert mating_unit3.male_mate_individual == Individual(['ped', 'male_mate3', '0', '0', '1', '0', 'null'])

    assert mating_unit1.female_mate_individual == Individual(['ped', 'female_mate1', '0', '0', '2', '0', 'null'])
    assert mating_unit2.female_mate_individual == Individual(['ped', 'female_mate2', '0', '0', '2', '0', 'null'])
    assert mating_unit3.female_mate_individual == Individual(['ped', 'female_mate3', '0', '0', '2', '0', 'null'])

    assert mating_unit1.sibship_unit_relation is None
    assert mating_unit2.sibship_unit_relation is None
    assert mating_unit3.sibship_unit_relation is None

    assert mating_unit1.generation_rank is None
    assert mating_unit2.generation_rank is None
    assert mating_unit3.generation_rank is None


def test_mating_unit_hash_code_method():
    individual1 = Individual(['ped', 'male_mate1', '0', '0', '1', '0', 'null'])
    individual2 = Individual(['ped', 'male_mate2', '0', '0', '1', '0', 'null'])
    individual3 = Individual(['ped', 'male_mate3', '0', '0', '1', '0', 'null'])
    individual4 = Individual(['ped', 'female_mate1', '0', '0', '2', '0', 'null'])
    individual5 = Individual(['ped', 'female_mate2', '0', '0', '2', '0', 'null'])
    individual6 = Individual(['ped', 'female_mate3', '0', '0', '2', '0', 'null'])

    mating_unit1 = MatingUnit('ped', individual1, individual4)
    mating_unit2 = MatingUnit('ped', individual2, individual5)
    mating_unit3 = MatingUnit('ped', individual3, individual6)

    assert isinstance(mating_unit1.__hash__(), int)
    assert isinstance(mating_unit2.__hash__(), int)
    assert isinstance(mating_unit3.__hash__(), int)

    assert mating_unit1.__hash__() == hash(mating_unit1.male_mate_individual) + hash(mating_unit1.female_mate_individual)
    assert mating_unit2.__hash__() == hash(mating_unit2.male_mate_individual) + hash(mating_unit2.female_mate_individual)
    assert mating_unit3.__hash__() == hash(mating_unit3.male_mate_individual) + hash(mating_unit3.female_mate_individual)


def test_mating_unit_equals_method():
    individual1 = Individual(['ped', 'male_mate1', '0', '0', '1', '0', 'null'])
    individual2 = Individual(['ped', 'male_mate2', '0', '0', '1', '0', 'null'])
    individual3 = Individual(['ped', 'male_mate3', '0', '0', '1', '0', 'null'])
    individual4 = Individual(['ped', 'female_mate1', '0', '0', '2', '0', 'null'])
    individual5 = Individual(['ped', 'female_mate2', '0', '0', '2', '0', 'null'])
    individual6 = Individual(['ped', 'female_mate3', '0', '0', '2', '0', 'null'])

    mating_unit1 = MatingUnit('ped', individual1, individual4)
    mating_unit2 = MatingUnit('ped', individual2, individual5)
    mating_unit3 = MatingUnit('ped', individual3, individual6)

    assert isinstance(mating_unit1.__eq__(None), bool)
    assert isinstance(mating_unit2.__eq__(None), bool)
    assert isinstance(mating_unit3.__eq__(None), bool)

    assert (mating_unit1 == None) is False
    assert (mating_unit2 == None) is False
    assert (mating_unit3 == None) is False

    assert (mating_unit1 == int) is False
    assert (mating_unit2 == int) is False
    assert (mating_unit3 == int) is False

    assert (mating_unit1 == float) is False
    assert (mating_unit2 == float) is False
    assert (mating_unit3 == float) is False
    
    assert (mating_unit1 == complex) is False
    assert (mating_unit2 == complex) is False
    assert (mating_unit3 == complex) is False

    assert (mating_unit1 == str) is False
    assert (mating_unit2 == str) is False
    assert (mating_unit3 == str) is False

    assert (mating_unit1 == mating_unit2) is False
    assert (mating_unit2 == mating_unit3) is False
    assert (mating_unit3 == mating_unit1) is False

    assert (mating_unit1 == mating_unit1) is True
    assert (mating_unit2 == mating_unit2) is True
    assert (mating_unit3 == mating_unit3) is True

    assert (mating_unit1 == MatingUnit('ped', individual1, individual4)) is True
    assert (mating_unit2 == MatingUnit('ped', individual2, individual5)) is True
    assert (mating_unit3 == MatingUnit('ped', individual3, individual6)) is True


def test_mating_unit_string_representation_method():
    individual1 = Individual(['ped', 'male_mate1', '0', '0', '1', '0', 'null'])
    individual2 = Individual(['ped', 'male_mate2', '0', '0', '1', '0', 'null'])
    individual3 = Individual(['ped', 'male_mate3', '0', '0', '1', '0', 'null'])
    individual4 = Individual(['ped', 'female_mate1', '0', '0', '2', '0', 'null'])
    individual5 = Individual(['ped', 'female_mate2', '0', '0', '2', '0', 'null'])
    individual6 = Individual(['ped', 'female_mate3', '0', '0', '2', '0', 'null'])

    mating_unit1 = MatingUnit('ped', individual1, individual4)
    mating_unit2 = MatingUnit('ped', individual2, individual5)
    mating_unit3 = MatingUnit('ped', individual3, individual6)

    assert isinstance(mating_unit1.__repr__(), str)
    assert isinstance(mating_unit2.__repr__(), str)
    assert isinstance(mating_unit3.__repr__(), str)

    assert str(mating_unit1) == repr(mating_unit1) == 'MU(male_mate1, female_mate1)'
    assert str(mating_unit2) == repr(mating_unit2) == 'MU(male_mate2, female_mate2)'
    assert str(mating_unit3) == repr(mating_unit3) == 'MU(male_mate3, female_mate3)'


def test_mating_unit_mating_string():
    individual1 = Individual(['ped', 'male_mate1', '0', '0', '1', '0', 'null'])
    individual2 = Individual(['ped', 'male_mate2', '0', '0', '1', '0', 'null'])
    individual3 = Individual(['ped', 'male_mate3', '0', '0', '1', '0', 'null'])
    individual4 = Individual(['ped', 'female_mate1', '0', '0', '2', '0', 'null'])
    individual5 = Individual(['ped', 'female_mate2', '0', '0', '2', '0', 'null'])
    individual6 = Individual(['ped', 'female_mate3', '0', '0', '2', '0', 'null'])

    mating_unit1 = MatingUnit('ped', individual1, individual4)
    mating_unit2 = MatingUnit('ped', individual2, individual5)
    mating_unit3 = MatingUnit('ped', individual3, individual6)

    assert isinstance(mating_unit1.mating_string(), str)
    assert isinstance(mating_unit2.mating_string(), str)
    assert isinstance(mating_unit3.mating_string(), str)

    assert mating_unit1.mating_string() == '(male_mate1, female_mate1)'
    assert mating_unit2.mating_string() == '(male_mate2, female_mate2)'
    assert mating_unit3.mating_string() == '(male_mate3, female_mate3)'


def test_sibship_unit_constructor():
    sibship_unit1 = SibshipUnit('pedigree')
    sibship_unit2 = SibshipUnit('pedigree')
    sibship_unit3 = SibshipUnit('pedigree')
    
    assert isinstance(sibship_unit1, SibshipUnit)
    assert isinstance(sibship_unit2, SibshipUnit)
    assert isinstance(sibship_unit3, SibshipUnit)

    assert 'sibship_unit1' in locals()
    assert 'sibship_unit2' in locals()
    assert 'sibship_unit3' in locals()

    with pytest.raises(AssertionError):
        SibshipUnit(None)
        SibshipUnit(bool)
        SibshipUnit(int)
        SibshipUnit(float)
        SibshipUnit(complex)

        SibshipUnit('pedigree', bool)
        SibshipUnit('pedigree', int)
        SibshipUnit('pedigree', float)
        SibshipUnit('pedigree', complex)
        SibshipUnit('pedigree', str)


def test_sibship_unit_destructor():
    sibship_unit1 = SibshipUnit('pedigree')
    sibship_unit2 = SibshipUnit('pedigree')
    sibship_unit3 = SibshipUnit('pedigree')

    del sibship_unit1
    del sibship_unit2
    del sibship_unit3

    assert 'sibship_unit1' not in locals()
    assert 'sibship_unit2' not in locals()
    assert 'sibship_unit3' not in locals()


def test_sibship_unit_properties():
    sibship_unit1 = SibshipUnit('pedigree1')
    sibship_unit2 = SibshipUnit('pedigree2')
    sibship_unit3 = SibshipUnit('pedigree3')

    assert hasattr(sibship_unit1, 'pedigree_identifier')
    assert hasattr(sibship_unit2, 'pedigree_identifier')
    assert hasattr(sibship_unit3, 'pedigree_identifier')

    assert hasattr(sibship_unit1, 'siblings_individuals')
    assert hasattr(sibship_unit2, 'siblings_individuals')
    assert hasattr(sibship_unit3, 'siblings_individuals')

    assert hasattr(sibship_unit1, 'siblings_extended')
    assert hasattr(sibship_unit2, 'siblings_extended')
    assert hasattr(sibship_unit3, 'siblings_extended')

    assert hasattr(sibship_unit1, 'mating_unit_relation')
    assert hasattr(sibship_unit2, 'mating_unit_relation')
    assert hasattr(sibship_unit3, 'mating_unit_relation')

    assert hasattr(sibship_unit1, 'generation_rank')
    assert hasattr(sibship_unit2, 'generation_rank')
    assert hasattr(sibship_unit3, 'generation_rank')

    assert isinstance(sibship_unit1.pedigree_identifier, str)
    assert isinstance(sibship_unit2.pedigree_identifier, str)
    assert isinstance(sibship_unit3.pedigree_identifier, str)

    assert isinstance(sibship_unit1.siblings_individuals, list)
    assert isinstance(sibship_unit2.siblings_individuals, list)
    assert isinstance(sibship_unit3.siblings_individuals, list)

    assert isinstance(sibship_unit1.siblings_extended, list)
    assert isinstance(sibship_unit2.siblings_extended, list)
    assert isinstance(sibship_unit3.siblings_extended, list)

    assert isinstance(sibship_unit1.mating_unit_relation, (MatingUnit, type(None)))
    assert isinstance(sibship_unit2.mating_unit_relation, (MatingUnit, type(None)))
    assert isinstance(sibship_unit3.mating_unit_relation, (MatingUnit, type(None)))

    assert isinstance(sibship_unit1.generation_rank, (int, type(None)))
    assert isinstance(sibship_unit2.generation_rank, (int, type(None)))
    assert isinstance(sibship_unit3.generation_rank, (int, type(None)))

    assert sibship_unit1.pedigree_identifier == 'pedigree1'
    assert sibship_unit2.pedigree_identifier == 'pedigree2'
    assert sibship_unit3.pedigree_identifier == 'pedigree3'

    assert sibship_unit1.siblings_individuals == list()
    assert sibship_unit2.siblings_individuals == list()
    assert sibship_unit3.siblings_individuals == list()

    assert sibship_unit1.siblings_extended == list()
    assert sibship_unit2.siblings_extended == list()
    assert sibship_unit3.siblings_extended == list()

    assert len(sibship_unit1.siblings_individuals) == 0
    assert len(sibship_unit2.siblings_individuals) == 0
    assert len(sibship_unit3.siblings_individuals) == 0

    assert len(sibship_unit1.siblings_extended) == 0
    assert len(sibship_unit2.siblings_extended) == 0
    assert len(sibship_unit3.siblings_extended) == 0

    assert sibship_unit1.mating_unit_relation is None
    assert sibship_unit2.mating_unit_relation is None
    assert sibship_unit3.mating_unit_relation is None

    assert sibship_unit1.generation_rank is None
    assert sibship_unit2.generation_rank is None
    assert sibship_unit3.generation_rank is None


def test_sibship_unit_deleters():
    sibship_unit1 = SibshipUnit('pedigree1')
    sibship_unit2 = SibshipUnit('pedigree2')
    sibship_unit3 = SibshipUnit('pedigree3')

    del sibship_unit1.pedigree_identifier
    del sibship_unit2.pedigree_identifier
    del sibship_unit3.pedigree_identifier

    del sibship_unit1.siblings_individuals
    del sibship_unit2.siblings_individuals
    del sibship_unit3.siblings_individuals

    del sibship_unit1.siblings_extended
    del sibship_unit2.siblings_extended
    del sibship_unit3.siblings_extended

    del sibship_unit1.mating_unit_relation
    del sibship_unit2.mating_unit_relation
    del sibship_unit3.mating_unit_relation

    del sibship_unit1.generation_rank
    del sibship_unit2.generation_rank
    del sibship_unit3.generation_rank

    assert not hasattr(sibship_unit1, 'pedigree_identifier')
    assert not hasattr(sibship_unit2, 'pedigree_identifier')
    assert not hasattr(sibship_unit3, 'pedigree_identifier')

    assert not hasattr(sibship_unit1, 'siblings_individuals')
    assert not hasattr(sibship_unit2, 'siblings_individuals')
    assert not hasattr(sibship_unit3, 'siblings_individuals')

    assert not hasattr(sibship_unit1, 'siblings_extended')
    assert not hasattr(sibship_unit2, 'siblings_extended')
    assert not hasattr(sibship_unit3, 'siblings_extended')

    assert not hasattr(sibship_unit1, 'mating_unit_relation')
    assert not hasattr(sibship_unit2, 'mating_unit_relation')
    assert not hasattr(sibship_unit3, 'mating_unit_relation')

    assert not hasattr(sibship_unit1, 'generation_rank')
    assert not hasattr(sibship_unit2, 'generation_rank')
    assert not hasattr(sibship_unit3, 'generation_rank')
