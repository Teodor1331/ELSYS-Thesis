import sys, pytest
sys.path.append('..')

from FamilyUnits import Individual
from FamilyUnits import MatingUnit
from FamilyUnits import SibshipUnit


def test_individual_instance():
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


def test_individual_constructor():
    with pytest.raises(AssertionError):
        Individual(0)
        Individual(0.0)
        Individual('Hello, World!')


def test_individual_properties():
    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'null'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'null'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'null'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'null'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'null'])

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
