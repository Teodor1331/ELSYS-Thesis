import sys
import pytest

sys.path.append('..')

from pedigree_builder import Loader
from pedigree_builder import Builder
from pedigree_units import Individual
from pedigree_family import PedigreeFamily

@pytest.fixture(name='loader1')
def fixture_loader1() -> Loader:
    return Loader('../../Examples/CSV Examples/Pedigree1.csv')


@pytest.fixture(name='loader2')
def fixture_loader2() -> Loader:
    return Loader('../../Examples/PED Examples/Pedigree1.ped')


@pytest.fixture(name='loader3')
def fixture_loader3() -> Loader:
    return Loader('../../Examples/TXT Examples/Pedigree1.txt')


def test_loader_constructor(loader1, loader2, loader3):
    assert isinstance(loader1, Loader)
    assert isinstance(loader2, Loader)
    assert isinstance(loader3, Loader)

    assert 'loader1' in locals()
    assert 'loader2' in locals()
    assert 'loader3' in locals()

    with pytest.raises(AssertionError):
        Loader(None), Loader(bool)
        Loader(int), Loader(float), Loader(complex)
        Loader(bytes), Loader(bytearray), Loader(str)
        Loader(list), Loader(tuple), Loader(range)
        Loader(set), Loader(frozenset), Loader(dict)
        Loader('Hello, World!')


def test_loader_constants():
    pedigree_columns = {}
    pedigree_columns['pedigree_identifier']     = 0
    pedigree_columns['individual_identifier']   = 1
    pedigree_columns['individual_father']       = 2
    pedigree_columns['individual_mother']       = 3
    pedigree_columns['individual_sex']          = 4
    pedigree_columns['individual_status']       = 5
    pedigree_columns['individual_role']         = 6

    assert Loader.PEDIGREE_COLUMNS              == pedigree_columns
    assert Loader.TAB_SEPARATED_EXTENSIONS      == ['.txt', '.ped']
    assert Loader.COMMA_SEPARATED_EXTENSIONS    == ['.csv']


def test_loader_destructor():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    del loader1
    del loader2
    del loader3

    assert 'loader1' not in locals()
    assert 'loader2' not in locals()
    assert 'loader3' not in locals()


def test_loader_properties():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    assert hasattr(loader1, 'file_path')
    assert hasattr(loader2, 'file_path')
    assert hasattr(loader3, 'file_path')

    assert hasattr(loader1, 'file_name')
    assert hasattr(loader2, 'file_name')
    assert hasattr(loader3, 'file_name')

    assert hasattr(loader1, 'file_stem')
    assert hasattr(loader2, 'file_stem')
    assert hasattr(loader3, 'file_stem')

    assert hasattr(loader1, 'file_suffix')
    assert hasattr(loader2, 'file_suffix')
    assert hasattr(loader3, 'file_suffix')

    assert hasattr(loader1, 'file_data')
    assert hasattr(loader2, 'file_data')
    assert hasattr(loader3, 'file_data')

    assert isinstance(loader1.file_path, str)
    assert isinstance(loader2.file_path, str)
    assert isinstance(loader3.file_path, str)

    assert isinstance(loader1.file_name, str)
    assert isinstance(loader2.file_name, str)
    assert isinstance(loader3.file_name, str)

    assert isinstance(loader1.file_stem, str)
    assert isinstance(loader2.file_stem, str)
    assert isinstance(loader3.file_stem, str)

    assert isinstance(loader1.file_suffix, str)
    assert isinstance(loader2.file_suffix, str)
    assert isinstance(loader3.file_suffix, str)

    assert isinstance(loader1.file_data, list)
    assert isinstance(loader2.file_data, list)
    assert isinstance(loader3.file_data, list)

    assert loader1.file_path == '../../Examples/CSV Examples/Pedigree1.csv'
    assert loader2.file_path == '../../Examples/PED Examples/Pedigree1.ped'
    assert loader3.file_path == '../../Examples/TXT Examples/Pedigree1.txt'

    assert loader1.file_name == 'Pedigree1.csv'
    assert loader2.file_name == 'Pedigree1.ped'
    assert loader3.file_name == 'Pedigree1.txt'

    assert loader1.file_stem == 'Pedigree1'
    assert loader2.file_stem == 'Pedigree1'
    assert loader3.file_stem == 'Pedigree1'

    assert loader1.file_suffix == '.csv'
    assert loader2.file_suffix == '.ped'
    assert loader3.file_suffix == '.txt'

    common_file_data = [
        ['ped', 'father', '0', '0', '1', '2', 'prb'],
        ['ped', 'mother', '0', '0', '2', '1', 'null'],
        ['ped', 'son1', 'father', 'mother', '1', '2', 'null'],
        ['ped', 'son2', 'father', 'mother', '1', '1', 'null'],
        ['ped', 'dau1', 'father', 'mother', '2', '2', 'null'],
        ['ped', 'dau2', 'father', 'mother', '2', '1', 'null']
    ]

    assert loader1.file_data == common_file_data
    assert loader2.file_data == common_file_data
    assert loader3.file_data == common_file_data


def test_loader_deleters():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    del loader1.file_path
    del loader2.file_path
    del loader3.file_path

    del loader1.file_name
    del loader2.file_name
    del loader3.file_name

    del loader1.file_stem
    del loader2.file_stem
    del loader3.file_stem

    del loader1.file_suffix
    del loader2.file_suffix
    del loader3.file_suffix

    del loader1.file_data
    del loader2.file_data
    del loader3.file_data

    assert not hasattr(loader1, 'file_path')
    assert not hasattr(loader2, 'file_path')
    assert not hasattr(loader3, 'file_path')

    assert not hasattr(loader1, 'file_name')
    assert not hasattr(loader2, 'file_name')
    assert not hasattr(loader3, 'file_name')

    assert not hasattr(loader1, 'file_stem')
    assert not hasattr(loader2, 'file_stem')
    assert not hasattr(loader3, 'file_stem')

    assert not hasattr(loader1, 'file_suffix')
    assert not hasattr(loader2, 'file_suffix')
    assert not hasattr(loader3, 'file_suffix')

    assert not hasattr(loader1, 'file_data')
    assert not hasattr(loader2, 'file_data')
    assert not hasattr(loader3, 'file_data')


def test_managing_tab_separated_file():
    loader = Loader('../../Examples/PED Examples/Pedigree1.ped')

    with pytest.raises(AssertionError):
        result = loader.manage_tab_separated(0)
        result = loader.manage_tab_separated(0.0)
        result = loader.manage_tab_separated('Hello, World!')

    with pytest.raises(ValueError):
        Loader('../../Examples/PED Examples/Pedigree7.ped')

    file_descriptor = open(loader.file_path)
    result = loader.manage_tab_separated(file_descriptor)

    expected_result = {
        'pedigree_identifier'   :   0,
        'individual_identifier' :   1,
        'individual_father'     :   2,
        'individual_mother'     :   3,
        'individual_sex'        :   4,
        'individual_status'     :   5,
        'individual_role'       :   6,
    }

    assert isinstance(result, dict)
    assert result == expected_result

    file_descriptor.close()


def test_manage_comma_separated_file():
    loader = Loader('../../Examples/CSV Examples/Pedigree1.csv')

    with pytest.raises(AssertionError):
        result = loader.manage_comma_separated(0)
        result = loader.manage_comma_separated(0.0)
        result = loader.manage_comma_separated('Hello, World!')

    with pytest.raises(StopIteration):
        Loader('../../Examples/CSV Examples/Pedigree7.csv')

    with pytest.raises(ValueError):
        Loader('../../Examples/CSV Examples/Pedigree2.csv')

    file_descriptor = open(loader.file_path)
    result = loader.manage_comma_separated(file_descriptor)

    expected_result = {
        'pedigree_identifier'   :   0,
        'individual_identifier' :   1,
        'individual_father'     :   2,
        'individual_mother'     :   3,
        'individual_sex'        :   4,
        'individual_status'     :   5,
        'individual_role'       :   6,
    }

    assert isinstance(result, dict)
    assert result == expected_result

    file_descriptor.close()


def test_reading_file_data():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')

    expected_result = [
        ['ped', 'father', '0', '0', '1', '2', 'prb'],
        ['ped', 'mother', '0', '0', '2', '1', 'null'],
        ['ped', 'son1', 'father', 'mother', '1', '2', 'null'],
        ['ped', 'son2', 'father', 'mother', '1', '1', 'null'],
        ['ped', 'dau1', 'father', 'mother', '2', '2', 'null'],
        ['ped', 'dau2', 'father', 'mother', '2', '1', 'null']
    ]

    result1 = loader1.read_file_data()
    result2 = loader2.read_file_data()

    assert isinstance(result1, list)
    assert isinstance(result2, list)

    for list_item in result1:
        assert isinstance(list_item, list)

        for item in list_item:
            assert isinstance(item, str)

    for list_item in result2:
        assert isinstance(list_item, list)

        for item in list_item:
            assert isinstance(item, str)

    assert result1 == expected_result
    assert result2 == expected_result


def test_builder_constructor():
    loader1 = Loader('../../Examples/TXT Examples/Pedigree1.txt')
    loader2 = Loader('../../Examples/TXT Examples/Pedigree2.txt')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree3.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    assert isinstance(builder1, Builder)
    assert isinstance(builder2, Builder)
    assert isinstance(builder3, Builder)

    assert 'builder1' in locals()
    assert 'builder2' in locals()
    assert 'builder3' in locals()

    with pytest.raises(AssertionError):
        Builder(None), Builder(bool)
        Builder(int), Builder(float), Builder(complex)
        Builder(bytes), Builder(bytearray), Builder(str)
        Builder(list), Builder(tuple), Builder(range)
        Builder(set), Builder(frozenset), Builder(dict)


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

    assert 'builder1' not in locals()
    assert 'builder2' not in locals()
    assert 'builder3' not in locals()


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


def test_builder_deleters():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    del builder1.file_data
    del builder2.file_data
    del builder3.file_data

    del builder1.file_pedigrees
    del builder2.file_pedigrees
    del builder3.file_pedigrees

    del builder1.file_individuals
    del builder2.file_individuals
    del builder3.file_individuals

    assert not hasattr(builder1, 'file_data')
    assert not hasattr(builder2, 'file_data')
    assert not hasattr(builder3, 'file_data')

    assert not hasattr(builder1, 'file_pedigrees')
    assert not hasattr(builder2, 'file_pedigrees')
    assert not hasattr(builder3, 'file_pedigrees')

    assert not hasattr(builder1, 'file_individuals')
    assert not hasattr(builder2, 'file_individuals')
    assert not hasattr(builder3, 'file_individuals')

    with pytest.raises(AttributeError):
        print(builder1.file_data)
        print(builder2.file_data)
        print(builder3.file_data)

        print(builder1.file_pedigrees)
        print(builder2.file_pedigrees)
        print(builder3.file_pedigrees)

        print(builder1.file_individuals)
        print(builder2.file_individuals)
        print(builder3.file_individuals)


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
