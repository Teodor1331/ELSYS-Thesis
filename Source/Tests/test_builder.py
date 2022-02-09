import sys, pytest
sys.path.append('..')

from loader import Loader
from Builder import Builder
from family_units import Individual
from pedigree_family import PedigreeFamily


def test_builder_instances():
    loader1 = Loader('../../Examples/TXT Examples/Pedigree1.txt')
    loader2 = Loader('../../Examples/TXT Examples/Pedigree2.txt')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree3.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    assert isinstance(builder1, Builder)
    assert isinstance(builder2, Builder)
    assert isinstance(builder3, Builder)


def test_builder_constructor():
    with pytest.raises(AssertionError):
        Builder(None)
        Builder(bool)
        Builder(int)
        Builder(float)
        Builder(complex)
        Builder(str)


def test_builder_destructor():
    loader1 = Loader('../../Examples/TXT Examples/Pedigree1.txt')
    loader2 = Loader('../../Examples/TXT Examples/Pedigree2.txt')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree3.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    del builder1
    del builder2
    del builder3

    with pytest.raises(NameError):
        print(builder1)
        print(builder2)
        print(builder3)


def test_builder_properties():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)
    
    assert hasattr(builder1, 'file_data')
    assert hasattr(builder1, 'file_pedigrees')
    assert hasattr(builder1, 'file_individuals')

    assert isinstance(builder1.file_data, list)
    assert isinstance(builder2.file_data, list)
    assert isinstance(builder3.file_data, list)

    assert isinstance(builder1.file_pedigrees, list)
    assert isinstance(builder2.file_pedigrees, list)
    assert isinstance(builder3.file_pedigrees, list)

    assert isinstance(builder1.file_individuals, list)
    assert isinstance(builder2.file_individuals, list)
    assert isinstance(builder3.file_individuals, list)

    assert len(builder1.file_data) == 6
    assert len(builder2.file_data) == 6
    assert len(builder3.file_data) == 6

    assert len(builder1.file_pedigrees) == 1
    assert len(builder2.file_pedigrees) == 1
    assert len(builder3.file_pedigrees) == 1

    assert len(builder1.file_individuals) == 6
    assert len(builder2.file_individuals) == 6
    assert len(builder3.file_individuals) == 6


def test_builder_build_file_units_method():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)


    assert isinstance(builder1.build_file_units(), tuple)
    assert isinstance(builder2.build_file_units(), tuple)
    assert isinstance(builder3.build_file_units(), tuple)

    assert isinstance(builder1.build_file_units()[0], list)
    assert isinstance(builder2.build_file_units()[0], list)
    assert isinstance(builder3.build_file_units()[0], list)

    assert isinstance(builder1.build_file_units()[1], list)
    assert isinstance(builder2.build_file_units()[1], list)
    assert isinstance(builder3.build_file_units()[1], list)

    assert len(builder1.build_file_units()) == 2
    assert len(builder2.build_file_units()) == 2
    assert len(builder3.build_file_units()) == 2

    assert len(builder1.build_file_units()[0]) == 1
    assert len(builder2.build_file_units()[0]) == 1
    assert len(builder3.build_file_units()[0]) == 1

    assert len(builder1.build_file_units()[1]) == 6
    assert len(builder2.build_file_units()[1]) == 6
    assert len(builder3.build_file_units()[1]) == 6

    assert isinstance(builder1.build_file_units()[0][0], PedigreeFamily)
    assert isinstance(builder2.build_file_units()[0][0], PedigreeFamily)
    assert isinstance(builder3.build_file_units()[0][0], PedigreeFamily)

    assert isinstance(builder1.build_file_units()[1][0], Individual)
    assert isinstance(builder1.build_file_units()[1][1], Individual)
    assert isinstance(builder1.build_file_units()[1][2], Individual)
    assert isinstance(builder1.build_file_units()[1][3], Individual)
    assert isinstance(builder1.build_file_units()[1][4], Individual)
    assert isinstance(builder1.build_file_units()[1][5], Individual)

    assert isinstance(builder2.build_file_units()[1][0], Individual)
    assert isinstance(builder2.build_file_units()[1][1], Individual)
    assert isinstance(builder2.build_file_units()[1][2], Individual)
    assert isinstance(builder2.build_file_units()[1][3], Individual)
    assert isinstance(builder2.build_file_units()[1][4], Individual)
    assert isinstance(builder2.build_file_units()[1][5], Individual)

    assert isinstance(builder3.build_file_units()[1][0], Individual)
    assert isinstance(builder3.build_file_units()[1][1], Individual)
    assert isinstance(builder3.build_file_units()[1][2], Individual)
    assert isinstance(builder3.build_file_units()[1][3], Individual)
    assert isinstance(builder3.build_file_units()[1][4], Individual)
    assert isinstance(builder3.build_file_units()[1][5], Individual)

    assert builder1.build_file_units()[0][0] == PedigreeFamily('ped')
    assert builder2.build_file_units()[0][0] == PedigreeFamily('ped')
    assert builder3.build_file_units()[0][0] == PedigreeFamily('ped')

    assert builder1.build_file_units()[1][0] == Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    assert builder1.build_file_units()[1][1] == Individual(['ped', 'mother', '0', '0', '2', '1', 'null'])
    assert builder1.build_file_units()[1][2] == Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'null'])
    assert builder1.build_file_units()[1][3] == Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'null'])
    assert builder1.build_file_units()[1][4] == Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'null'])
    assert builder1.build_file_units()[1][5] == Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'null'])

    assert builder2.build_file_units()[1][0] == Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    assert builder2.build_file_units()[1][1] == Individual(['ped', 'mother', '0', '0', '2', '1', 'null'])
    assert builder2.build_file_units()[1][2] == Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'null'])
    assert builder2.build_file_units()[1][3] == Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'null'])
    assert builder2.build_file_units()[1][4] == Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'null'])
    assert builder2.build_file_units()[1][5] == Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'null'])

    assert builder3.build_file_units()[1][0] == Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    assert builder3.build_file_units()[1][1] == Individual(['ped', 'mother', '0', '0', '2', '1', 'null'])
    assert builder3.build_file_units()[1][2] == Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'null'])
    assert builder3.build_file_units()[1][3] == Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'null'])
    assert builder3.build_file_units()[1][4] == Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'null'])
    assert builder3.build_file_units()[1][5] == Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'null'])


def test_builder_build_inner_units_method():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    assert isinstance(builder1.build_inner_units(), type(None))
    assert isinstance(builder2.build_inner_units(), type(None))
    assert isinstance(builder3.build_inner_units(), type(None))
