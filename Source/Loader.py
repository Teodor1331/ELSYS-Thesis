import re
import csv

from pathlib    import Path
from io         import TextIOWrapper


class Loader:
    PEDIGREE_COLUMNS = {
        'pedigree_identifier'       :   0,
        'individual_identifier'     :   1,
        'individual_father'         :   2,
        'individual_mother'         :   3,
        'individual_sex'            :   4,
        'individual_status'         :   5,
        'individual_role'           :   6,
    }

    TAB_SEPARATED_EXTENSIONS    =   ['.txt', '.ped']
    COMMA_SEPARATED_EXTENSIONS  =   ['.csv']

    def __init__(self, file_path) -> None:
        try:
            assert isinstance(file_path, str)
        except AssertionError:
            raise AssertionError("The file path is not a correct name!")
        
        try:
            self.__file_path    =   file_path
            self.__file_name    =   Path(file_path).name
            self.__file_stem    =   Path(file_path).stem
            self.__file_suffix  =   Path(file_path).suffix
            self.__file_data    =   self.read_file_data()
        except FileNotFoundError:
            raise Exception("The file was not found!")

    @property
    def file_path(self) -> str:
        return self.__file_path


    @property
    def file_name(self) -> str:
        return self.__file_name


    @property
    def file_stem(self) -> str:
        return self.__file_stem


    @property
    def file_suffix(self) -> str:
        return self.__file_suffix


    @property
    def file_data(self) -> list:
        return self.__file_data


    @file_path.setter
    def file_path(self, file_path) -> None:
        assert isinstance(file_path, str)
        self.__file_path = file_path


    @file_name.setter
    def file_name(self, file_name) -> None:
        assert isinstance(file_name, str)
        self.__file_name = file_name


    @file_stem.setter
    def file_stem(self, file_stem) -> None:
        assert isinstance(file_stem)
        self.__file_stem = file_stem


    @file_suffix.setter
    def file_suffix(self, file_suffix) -> None:
        assert isinstance(file_suffix, str)
        self.__file_suffix = file_suffix


    @file_data.setter
    def file_data(self, file_data) -> None:
        assert isinstance(file_data, list)
        self.__file_data = file_data


    @file_path.deleter
    def file_path(self) -> None:
        del self.__file_path


    @file_name.deleter
    def file_name(self) -> None:
        del self.__file_name


    @file_stem.deleter
    def file_stem(self) -> None:
        del self.__file_stem


    @file_suffix.deleter
    def file_suffix(self) -> None:
        del self.__file_suffix


    @file_data.deleter
    def file_data(self) -> None:
        del self.__file_data


    def __del__(self) -> None:
        del self.__file_path
        del self.__file_name
        del self.__file_stem
        del self.__file_suffix
        del self.__file_data


    def manage_tab_separated(self, file_object):
        assert isinstance(file_object, TextIOWrapper)
        dictionary_order    =   dict()

        header_line = file_object.readline()
        header_line = re.sub(' +', '\t', header_line)
        header_line = re.sub('\t+', '\t', header_line)
        header_line = header_line.strip('\n').split('\t')

        for column_name in header_line:
            if column_name[1:] in Loader.PEDIGREE_COLUMNS:
                dictionary_order[column_name[1:]] = header_line.index(column_name)
            else:
                raise ValueError("The column name", column_name[1:], "is not recognized!")

        return dictionary_order


    def manage_comma_separated(self, file_object):
        assert isinstance(file_object, TextIOWrapper)
        dictionary_order    =   dict()

        csv_reader = csv.reader(file_object)

        header_line = [column for column in next(csv_reader) if column != '']

        for column_name in header_line:
            if column_name in Loader.PEDIGREE_COLUMNS:
                dictionary_order[column_name] = header_line.index(column_name)
            else:
                raise ValueError("The column name", column_name, "is not recognized!")

        return dictionary_order


    def read_file_data(self):
        buffer_data =   list()
        file_data   =   list()
        file = open(self.file_path)

        if self.file_suffix.lower() in Loader.TAB_SEPARATED_EXTENSIONS:
            dictionary_order = self.manage_tab_separated(file)

            for file_line in file:
                file_line = re.sub(' +', '\t', file_line)
                file_line = re.sub('\t+', '\t', file_line)
                file_line = file_line.strip('\n').split('\t')
                buffer_data.append(file_line)
        elif self.file_suffix.lower() in Loader.COMMA_SEPARATED_EXTENSIONS:
            dictionary_order = self.manage_comma_separated(file)
            csv_reader = csv.reader(file)

            for file_line in csv_reader:
                buffer_data.append(file_line)
        else:
            raise ValueError("The format of the file is not recognized!")

        for file_line in buffer_data:
            ordered_line = list()

            for column_name in Loader.PEDIGREE_COLUMNS:
                ordered_line.append(file_line[dictionary_order.get(column_name)])

            file_data.append(ordered_line)

        file.close()
        return file_data
