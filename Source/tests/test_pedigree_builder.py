# This Python file uses the following encoding: UTF-8

"""Test module on the classes Loader and Builder."""

from collections import defaultdict

import inspect
import pytest
import os
import stat

from ..logic.pedigree_builder import Loader
from ..logic.pedigree_builder import Builder
from ..logic.pedigree_units import Individual
from ..logic.pedigree_family import PedigreeFamily


@pytest.fixture(name='loader1')
def fixture_loader1() -> Loader:
    """Return a fixture of Loader class with correct CSV file."""
    return Loader('../../Examples/CSV Examples/Pedigree1.csv')


@pytest.fixture(name='loader2')
def fixture_loader2() -> Loader:
    """Return a fixture of Loader class with correct PED file."""
    return Loader('../../Examples/PED Examples/Pedigree1.ped')


@pytest.fixture(name='loader3')
def fixture_loader3() -> Loader:
    """Return a fixture of Loader class with correct TXT file."""
    return Loader('../../Examples/TXT Examples/Pedigree1.txt')


@pytest.fixture(name='builder1')
def fixture_builder1(loader1) -> Builder:
    """Return a fixture of Builder class with correct CSV file."""
    assert isinstance(loader1, Loader)
    return Builder(loader1.file_data)


@pytest.fixture(name='builder2')
def fixture_builder2(loader2) -> Builder:
    """Return a fixture of Builder class with correct PED file."""
    assert isinstance(loader2, Loader)
    return Builder(loader2.file_data)


@pytest.fixture(name='builder3')
def fixture_builder3(loader3) -> Builder:
    """Return a fixture of Builder class with correct TXT file."""
    assert isinstance(loader3, Loader)
    return Builder(loader3.file_data)


@pytest.fixture(name='column_order')
def fixture_column_order() -> dict:
    return {
        'pedigree_identifier': 0,
        'individual_identifier': 1,
        'individual_father': 2,
        'individual_mother': 3,
        'individual_sex': 4,
        'individual_status': 5,
        'individual_role': 6,
    }


@pytest.fixture(name='valid_data')
def fixture_valid_data() -> list:
    return [
        ['ped', 'father', '0', '0', '1', '2', 'prb'],
        ['ped', 'mother', '0', '0', '2', '1', 'null'],
        ['ped', 'son1', 'father', 'mother', '1', '2', 'null'],
        ['ped', 'son2', 'father', 'mother', '1', '1', 'null'],
        ['ped', 'dau1', 'father', 'mother', '2', '2', 'null'],
        ['ped', 'dau2', 'father', 'mother', '2', '1', 'null']
    ]


@pytest.fixture(name='invalid_dictionary')
def fixture_invalid_dictionary() -> defaultdict:
    return defaultdict(list, {
        'ped': [
            ['ped', 'father', '0', '0', '1', '2', 'prb'],
            ['ped', 'mother', '0', '0', '2', '1', 'null']
        ]
    })


@pytest.fixture(name='valid_dictionary')
def fixture_valid_dictionary() -> defaultdict:
    return defaultdict(list, {
        'ped': [
            ['ped', 'father', '0', '0', '1', '2', 'prb'],
            ['ped', 'mother', '0', '0', '2', '1', 'null'],
            ['ped', 'son', 'father', 'mother', '1', '2', 'null'],
            ['ped', 'dau', 'father', 'mother', '2', '2', 'null'],
        ]
    })


@pytest.fixture(name='invalid_data2')
def fixture_invalid_data2() -> list:
    return [
        ['ped', 'father', '0', '0', '1', '2', 'null'],
        ['ped', 'mother', '0', '0', '2', '1', 'null'],
        ['ped', 'son1', 'father', 'mother', '1', '2', 'null'],
        ['ped', 'son2', 'father', 'mother', '1', '1', 'null'],
        ['ped', 'dau1', 'father', 'mother', '2', '2', 'null'],
        ['ped', 'dau2', 'father', 'mother', '2', '1', 'null']
    ]


def test_imported_modules():
    """Test Module Inner Imports."""
    assert inspect.ismodule(pytest)
    assert inspect.ismodule(inspect)
    assert inspect.ismodule(os)
    assert inspect.ismodule(stat)


def test_loader_instances(loader1, loader2, loader3):
    """Test Loader Class Instances."""
    assert isinstance(loader1, Loader)
    assert isinstance(loader2, Loader)
    assert isinstance(loader3, Loader)
    assert inspect.isclass(Loader)


def test_loader_constructor():
    """Test Loader Class Constructor."""
    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader(None), Loader(bool), Loader(str)
        Loader(int), Loader(float), Loader(complex)
        Loader(bytes), Loader(bytearray), Loader(memoryview)
        Loader(list), Loader(tuple), Loader(range)
        Loader(set), Loader(frozenset), Loader(dict)

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 1

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader('Hello, World!')
        Loader('Hello, Python!')
        Loader('Python World!')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 1

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader('../../Examples/Others/Example Folder')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 1

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        os.chmod('../../Examples/Others/Example.ped', ~stat.S_IRUSR)
        Loader('../../Examples/Others/Example.ped')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 1

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader('../../Examples/PED Examples/Pedigree4.ped')
        Loader('../../Examples/PED Examples/Pedigree5.ped')
        Loader('../../Examples/PED Examples/Pedigree6.ped')
        Loader('../../Examples/PED Examples/Pedigree7.ped')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 1

    os.chmod('../../Examples/Others/Example.ped', stat.S_IRUSR)


def test_loader_constants():
    """Test Loader Class Constants."""
    pedigree_columns = {
        'pedigree_identifier': 0,
        'individual_identifier': 1,
        'individual_father': 2,
        'individual_mother': 3,
        'individual_sex': 4,
        'individual_status': 5,
        'individual_role': 6
    }

    assert isinstance(Loader.PEDIGREE_COLUMNS, dict)
    assert isinstance(Loader.TAB_SEPARATED_EXTENSIONS, list)
    assert isinstance(Loader.COMMA_SEPARATED_EXTENSIONS, list)

    assert len(Loader.PEDIGREE_COLUMNS) == 7
    assert len(Loader.TAB_SEPARATED_EXTENSIONS) == 2
    assert len(Loader.COMMA_SEPARATED_EXTENSIONS) == 1

    assert Loader.PEDIGREE_COLUMNS == pedigree_columns
    assert Loader.TAB_SEPARATED_EXTENSIONS == ['.txt', '.ped']
    assert Loader.COMMA_SEPARATED_EXTENSIONS == ['.csv']


def test_loader_properties(loader1, loader2, loader3, valid_data):
    """Test Loader Class Properties."""
    assert isinstance(loader1, Loader)
    assert isinstance(loader2, Loader)
    assert isinstance(loader3, Loader)

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

    assert loader1.file_data == valid_data
    assert loader2.file_data == valid_data
    assert loader3.file_data == valid_data


def test_loader_methods(loader1, loader2, loader3):
    """Test Loader Class Methods."""
    assert isinstance(loader1, Loader)
    assert isinstance(loader2, Loader)
    assert isinstance(loader3, Loader)

    assert inspect.ismethod(loader1.manage_tabbed_separated)
    assert inspect.ismethod(loader2.manage_tabbed_separated)
    assert inspect.ismethod(loader3.manage_tabbed_separated)

    assert inspect.ismethod(loader1.manage_comma_separated)
    assert inspect.ismethod(loader2.manage_comma_separated)
    assert inspect.ismethod(loader3.manage_comma_separated)

    assert inspect.ismethod(loader1.read_file_data)
    assert inspect.ismethod(loader2.read_file_data)
    assert inspect.ismethod(loader3.read_file_data)

    assert inspect.ismethod(loader1.validate_file_data)
    assert inspect.ismethod(loader2.validate_file_data)
    assert inspect.ismethod(loader3.validate_file_data)

    assert inspect.isfunction(loader1.validate_number_individuals)
    assert inspect.isfunction(loader2.validate_number_individuals)
    assert inspect.isfunction(loader3.validate_number_individuals)

    assert inspect.isfunction(loader1.validate_context_individuals)
    assert inspect.isfunction(loader2.validate_context_individuals)
    assert inspect.isfunction(loader3.validate_context_individuals)

    assert inspect.isfunction(loader1.find_parent_individual)
    assert inspect.isfunction(loader2.find_parent_individual)
    assert inspect.isfunction(loader3.find_parent_individual)

    assert inspect.isfunction(loader1.find_proband_individual)
    assert inspect.isfunction(loader2.find_proband_individual)
    assert inspect.isfunction(loader3.find_proband_individual)


def test_managing_tabbed_separated_file_method(column_order):
    """Test Loader Managing Tabbed Separated File Method."""
    loader = Loader('../../Examples/PED Examples/Pedigree1.ped')

    with pytest.raises(AssertionError, match='The file object is not valid!'):
        loader.manage_tabbed_separated(None)
        loader.manage_tabbed_separated(bool)
        loader.manage_tabbed_separated(str)
        loader.manage_tabbed_separated(int)
        loader.manage_tabbed_separated(float)
        loader.manage_tabbed_separated(complex)
        loader.manage_tabbed_separated(bytes)
        loader.manage_tabbed_separated(bytearray)
        loader.manage_tabbed_separated(memoryview)
        loader.manage_tabbed_separated(list)
        loader.manage_tabbed_separated(tuple)
        loader.manage_tabbed_separated(range)
        loader.manage_tabbed_separated(set)
        loader.manage_tabbed_separated(tuple)
        loader.manage_tabbed_separated(dict)
        loader.manage_tabbed_separated('Hello, World!')

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader('../../Examples/PED Examples/Pedigree2.ped')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 2

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader('../../Examples/PED Examples/Pedigree3.ped')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 2

    file_descriptor = open(loader.file_path)
    result = loader.manage_tabbed_separated(file_descriptor)

    assert isinstance(result, dict)
    assert result == column_order
    file_descriptor.close()


def test_manage_comma_separated_file_method(column_order):
    """Test Loader Managing Comma Separated File Method."""
    loader = Loader('../../Examples/CSV Examples/Pedigree1.csv')

    with pytest.raises(AssertionError, match='The file object is not valid!'):
        loader.manage_comma_separated(None)
        loader.manage_comma_separated(bool)
        loader.manage_comma_separated(str)
        loader.manage_comma_separated(int)
        loader.manage_comma_separated(float)
        loader.manage_comma_separated(complex)
        loader.manage_comma_separated(bytes)
        loader.manage_comma_separated(bytearray)
        loader.manage_comma_separated(memoryview)
        loader.manage_comma_separated(list)
        loader.manage_comma_separated(tuple)
        loader.manage_comma_separated(range)
        loader.manage_comma_separated(set)
        loader.manage_comma_separated(tuple)
        loader.manage_comma_separated(dict)
        loader.manage_comma_separated('Hello, World!')

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader('../../Examples/CSV Examples/Pedigree3.csv')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 3

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Loader('../../Examples/CSV Examples/Pedigree2.csv')

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 2

    file_descriptor = open(loader.file_path)
    result = loader.manage_comma_separated(file_descriptor)

    assert isinstance(result, dict)
    assert result == column_order
    file_descriptor.close()


def test_reading_file_data_method():
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


def test_validate_file_data_method():
    pass


def test_validate_number_individuals_method():
    pass


def test_validate_context_individuals_method():
    pass


def test_find_parent_individual_method():
    pass


def test_find_proband_individual_method():
    pass


def test_builder_instances(builder1, builder2, builder3):
    assert isinstance(builder1, Builder)
    assert isinstance(builder2, Builder)
    assert isinstance(builder3, Builder)
    assert inspect.isclass(Builder)


def test_builder_constructor():
    """Test Builder Class Constructor."""

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        Builder(None), Builder(bool), Builder(str)
        Builder(int), Builder(float), Builder(complex)
        Builder(bytes), Builder(bytearray), Builder(memoryview)
        Builder(list), Builder(tuple), Builder(range)
        Builder(set), Builder(frozenset), Builder(dict)

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 4


def test_builder_properties(builder1, builder2, builder3):
    assert isinstance(builder1, Builder)
    assert isinstance(builder2, Builder)
    assert isinstance(builder3, Builder)

    assert hasattr(builder1, 'file_data')
    assert hasattr(builder2, 'file_data')
    assert hasattr(builder3, 'file_data')

    assert hasattr(builder1, 'file_pedigrees')
    assert hasattr(builder2, 'file_pedigrees')
    assert hasattr(builder3, 'file_pedigrees')

    assert hasattr(builder1, 'file_individuals')
    assert hasattr(builder2, 'file_individuals')
    assert hasattr(builder3, 'file_individuals')

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


def test_builder_build_file_units_method(builder1, builder2, builder3):
    assert isinstance(builder1, Builder)
    assert isinstance(builder2, Builder)
    assert isinstance(builder3, Builder)

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


def test_builder_build_inner_units_method(builder1, builder2, builder3):
    assert isinstance(builder1, Builder)
    assert isinstance(builder2, Builder)
    assert isinstance(builder3, Builder)

    assert isinstance(builder1.build_inner_units(), type(None))
    assert isinstance(builder2.build_inner_units(), type(None))
    assert isinstance(builder3.build_inner_units(), type(None))
