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


def test_loader_constructor():
    with pytest.raises(AssertionError):
        Loader(0)
        Loader(0.0)

    with pytest.raises(FileNotFoundError):
        Loader('Hello, World!')


def test_loader_destructor():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    del loader1
    del loader2
    del loader3

    with pytest.raises(NameError):
        print(loader1)
        print(loader2)
        print(loader3)


def test_loader_properties():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

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

    with pytest.raises(AttributeError):
        print(loader1.file_path)
        print(loader2.file_path)
        print(loader3.file_path)

        print(loader1.file_name)
        print(loader2.file_name)
        print(loader3.file_name)

        print(loader1.file_stem)
        print(loader2.file_stem)
        print(loader3.file_stem)

        print(loader1.file_suffix)
        print(loader2.file_suffix)
        print(loader3.file_suffix)

        print(loader1.file_data)
        print(loader2.file_data)
        print(loader3.file_data)


def test_managing_tab_separated_file():
    loader = Loader('../../Examples/PED Examples/Pedigree1.ped')

    with pytest.raises(AssertionError):
        result = loader.manage_tab_separated(0)
        result = loader.manage_tab_separated(0.0)
        result = loader.manage_tab_separated('Hello, World!')

    with pytest.raises(ValueError):
        exception_loader = Loader('../../Examples/PED Examples/Pedigree7.ped')

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
        exception_loader = Loader('../../Examples/CSV Examples/Pedigree7.csv')

    with pytest.raises(ValueError):
        exception_loader = Loader('../../Examples/CSV Examples/Pedigree2.csv')

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
    