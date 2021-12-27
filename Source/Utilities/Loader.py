import re
import csv

from pathlib    import Path
from io         import TextIOWrapper


PEDIGREE_COLUMNS = {
    "pedigree_identifier"       :   0,
    "individual_identifier"     :   1,
    "individual_father"         :   2,
    "individual_mother"         :   3,
    "individual_sex"            :   4,
    "individual_role"           :   5,
}


class Loader:
    TAB_SEPARATED   =   ['.txt', '.ped']
    COMMA_SEPARATED =   ['.csv']

    def __init__(self, file_path):
        assert isinstance(file_path, str)

        self.__file_path    =   file_path
        self.__file_name    =   Path(file_path).name
        self.__file_stem    =   Path(file_path).stem
        self.__file_suffix  =   Path(file_path).suffix
        self.__file_data    =   self.read_file_data()


    @property
    def file_path(self):
        return self.__file_path


    @property
    def file_name(self):
        return self.__file_name


    @property
    def file_stem(self):
        return self.__file_stem


    @property
    def file_suffix(self):
        return self.__file_suffix


    @property
    def file_data(self):
        return self.__file_data


    @file_path.deleter
    def file_path(self):
        del self.__file_path


    @file_name.deleter
    def file_name(self):
        del self.__file_name


    @file_stem.deleter
    def file_stem(self):
        del self.__file_stem


    @file_suffix.deleter
    def file_suffix(self):
        del self.__file_suffix


    @file_data.deleter
    def file_data(self):
        del self.__file_data


    def __del__(self):
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
            if column_name[1:] in PEDIGREE_COLUMNS:
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
            if column_name in PEDIGREE_COLUMNS:
                dictionary_order[column_name] = header_line.index(column_name)
            else:
                raise ValueError("The column name", column_name, "is not recognized!")

        return dictionary_order


    def read_file_data(self):
        buffer_data =   list()
        file_data   =   list()
        file = open(self.file_path)

        if self.file_suffix.lower() in Loader.TAB_SEPARATED:
            dictionary_order = self.manage_tab_separated(file)

            for file_line in file:
                file_line = re.sub(' +', '\t', file_line)
                file_line = re.sub('\t+', '\t', file_line)
                file_line = file_line.strip('\n').split('\t')
                buffer_data.append(file_line)
        elif self.file_suffix.lower() in Loader.COMMA_SEPARATED:
            dictionary_order = self.manage_comma_separated(file)
            csv_reader = csv.reader(file)

            for file_line in csv_reader:
                buffer_data.append(file_line)
        else:
            raise ValueError("The format of the file is not recognized!")

        for file_line in buffer_data:
            ordered_line = list()

            for column_name in PEDIGREE_COLUMNS:
                ordered_line.append(file_line[dictionary_order.get(column_name)])

            file_data.append(ordered_line)

        file.close()
        return file_data
