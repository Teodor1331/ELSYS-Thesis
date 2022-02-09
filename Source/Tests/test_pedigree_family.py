import sys, pytest
sys.path.append('..')

from pedigree_family import PedigreeFamily


def test_pedigree_family_instances():
    pedigree_family1 = PedigreeFamily('pedigree_family1')
    pedigree_family2 = PedigreeFamily('pedigree_family2')
    pedigree_family3 = PedigreeFamily('pedigree_family3')

    assert isinstance(pedigree_family1, PedigreeFamily)
    assert isinstance(pedigree_family2, PedigreeFamily)
    assert isinstance(pedigree_family3, PedigreeFamily)


def test_pedigree_family_constructor():
    with pytest.raises(AssertionError):
        PedigreeFamily(None)
        PedigreeFamily(bool)
        PedigreeFamily(int)
        PedigreeFamily(float)
        PedigreeFamily(complex)


def test_pedigree_family_destructor():
    pedigree_family1 = PedigreeFamily('pedigree_family1')
    pedigree_family2 = PedigreeFamily('pedigree_family2')
    pedigree_family3 = PedigreeFamily('pedigree_family3')

    del pedigree_family1
    del pedigree_family2
    del pedigree_family3

    assert 'pedigree_family1' not in locals()
    assert 'pedigree_family2' not in locals()
    assert 'pedigree_family3' not in locals()


def test_pedigree_family_properties():
    pedigree_family1 = PedigreeFamily('pedigree_family1')
    pedigree_family2 = PedigreeFamily('pedigree_family2')
    pedigree_family3 = PedigreeFamily('pedigree_family3')

    assert hasattr(pedigree_family1, 'pedigree_identifier')
    assert hasattr(pedigree_family2, 'pedigree_identifier')
    assert hasattr(pedigree_family3, 'pedigree_identifier')

    assert hasattr(pedigree_family1, 'pedigree_individuals')
    assert hasattr(pedigree_family2, 'pedigree_individuals')
    assert hasattr(pedigree_family3, 'pedigree_individuals')

    assert hasattr(pedigree_family1, 'pedigree_mating_units')
    assert hasattr(pedigree_family2, 'pedigree_mating_units')
    assert hasattr(pedigree_family3, 'pedigree_mating_units')

    assert hasattr(pedigree_family1, 'pedigree_sibship_units')
    assert hasattr(pedigree_family2, 'pedigree_sibship_units')
    assert hasattr(pedigree_family3, 'pedigree_sibship_units')

    assert hasattr(pedigree_family1, 'min_generation_rank')
    assert hasattr(pedigree_family2, 'min_generation_rank')
    assert hasattr(pedigree_family3, 'min_generation_rank')

    assert hasattr(pedigree_family1, 'max_generation_rank')
    assert hasattr(pedigree_family2, 'max_generation_rank')
    assert hasattr(pedigree_family3, 'max_generation_rank')

    assert isinstance(pedigree_family1.pedigree_identifier, str)
    assert isinstance(pedigree_family2.pedigree_identifier, str)
    assert isinstance(pedigree_family3.pedigree_identifier, str)

    assert isinstance(pedigree_family1.pedigree_individuals, dict)
    assert isinstance(pedigree_family2.pedigree_individuals, dict)
    assert isinstance(pedigree_family3.pedigree_individuals, dict)

    assert isinstance(pedigree_family1.pedigree_mating_units, dict)
    assert isinstance(pedigree_family2.pedigree_mating_units, dict)
    assert isinstance(pedigree_family3.pedigree_mating_units, dict)

    assert isinstance(pedigree_family1.pedigree_sibship_units, dict)
    assert isinstance(pedigree_family2.pedigree_sibship_units, dict)
    assert isinstance(pedigree_family3.pedigree_sibship_units, dict)

    assert isinstance(pedigree_family1.min_generation_rank, (int, type(None)))
    assert isinstance(pedigree_family2.min_generation_rank, (int, type(None)))
    assert isinstance(pedigree_family3.min_generation_rank, (int, type(None)))

    assert isinstance(pedigree_family1.max_generation_rank, (int, type(None)))
    assert isinstance(pedigree_family2.max_generation_rank, (int, type(None)))
    assert isinstance(pedigree_family3.max_generation_rank, (int, type(None)))

    assert pedigree_family1.pedigree_identifier == 'pedigree_family1'
    assert pedigree_family2.pedigree_identifier == 'pedigree_family2'
    assert pedigree_family3.pedigree_identifier == 'pedigree_family3'

    assert pedigree_family1.pedigree_individuals == dict()
    assert pedigree_family2.pedigree_individuals == dict()
    assert pedigree_family3.pedigree_individuals == dict()

    assert pedigree_family1.pedigree_mating_units == dict()
    assert pedigree_family2.pedigree_mating_units == dict()
    assert pedigree_family3.pedigree_mating_units == dict()

    assert pedigree_family1.pedigree_sibship_units == dict()
    assert pedigree_family2.pedigree_sibship_units == dict()
    assert pedigree_family3.pedigree_sibship_units == dict()

    assert len(pedigree_family1.pedigree_individuals) == 0
    assert len(pedigree_family2.pedigree_individuals) == 0
    assert len(pedigree_family3.pedigree_individuals) == 0

    assert len(pedigree_family1.pedigree_mating_units) == 0
    assert len(pedigree_family2.pedigree_mating_units) == 0
    assert len(pedigree_family3.pedigree_mating_units) == 0

    assert len(pedigree_family1.pedigree_sibship_units) == 0
    assert len(pedigree_family2.pedigree_sibship_units) == 0
    assert len(pedigree_family3.pedigree_sibship_units) == 0

    assert pedigree_family1.min_generation_rank is None
    assert pedigree_family2.min_generation_rank is None
    assert pedigree_family3.min_generation_rank is None

    assert pedigree_family1.max_generation_rank is None
    assert pedigree_family2.max_generation_rank is None
    assert pedigree_family3.max_generation_rank is None


def test_pedigree_family_deleters():
    pedigree_family1 = PedigreeFamily('pedigree_family1')
    pedigree_family2 = PedigreeFamily('pedigree_family2')
    pedigree_family3 = PedigreeFamily('pedigree_family3')

    del pedigree_family1.pedigree_identifier
    del pedigree_family2.pedigree_identifier
    del pedigree_family3.pedigree_identifier

    assert not hasattr(pedigree_family1, 'pedigree_identifier')
    assert not hasattr(pedigree_family2, 'pedigree_identifier')
    assert not hasattr(pedigree_family3, 'pedigree_identifier')


def test_pedigree_family_string_representation_method():
    pedigree_family1 = PedigreeFamily('pedigree_family1')
    pedigree_family2 = PedigreeFamily('pedigree_family2')
    pedigree_family3 = PedigreeFamily('pedigree_family3')

    assert isinstance(pedigree_family1.__repr__(), str)
    assert isinstance(pedigree_family2.__repr__(), str)
    assert isinstance(pedigree_family3.__repr__(), str)

    assert str(pedigree_family1) == repr(pedigree_family1) == 'pedigree_family1'
    assert str(pedigree_family2) == repr(pedigree_family2) == 'pedigree_family2'
    assert str(pedigree_family3) == repr(pedigree_family3) == 'pedigree_family3'
