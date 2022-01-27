import sys
import pytest


sys.path.append('..')


from Loader import Loader


def test_loader_instances():
    loader1 = Loader('../../Examples/TXT Examples/Pedigree1.txt')
    loader2 = Loader('../../Examples/TXT Examples/Pedigree2.txt')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree3.txt')

    assert isinstance(loader1, Loader)
    assert isinstance(loader2, Loader)
    assert isinstance(loader3, Loader)


def test_loader_constants():
    loader = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    pedigree_columns = dict()
    pedigree_columns['pedigree_identifier']     = 0
    pedigree_columns['individual_identifier']   = 1
    pedigree_columns['individual_father']       = 2
    pedigree_columns['individual_mother']       = 3
    pedigree_columns['individual_sex']          = 4
    pedigree_columns['individual_status']       = 5
    pedigree_columns['individual_role']         = 6

    assert loader.PEDIGREE_COLUMNS              == pedigree_columns
    assert loader.TAB_SEPARATED_EXTENSIONS      == ['.txt', '.ped']
    assert loader.COMMA_SEPARATED_EXTENSIONS    == ['.csv']


def test_loader_constructor():
    pass
    