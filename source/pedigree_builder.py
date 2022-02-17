"""The file contains the classes Loader and Builder.

This file contains the logic of reading a pedigree file
and building pedigree families with pedigree units.
"""

import os
import re
import csv

from pathlib import Path
from io import TextIOWrapper

from pedigree_units import Individual
from pedigree_family import PedigreeFamily


class Loader:
    """Class Name: Loader.

    This class is used to load the whole
    data from a pedigree file. The file
    can be tab spearated or comma separated.
    """

    PEDIGREE_COLUMNS = {
        'pedigree_identifier': 0,
        'individual_identifier': 1,
        'individual_father': 2,
        'individual_mother': 3,
        'individual_sex': 4,
        'individual_status': 5,
        'individual_role': 6,
    }

    TAB_SEPARATED_EXTENSIONS = ['.txt', '.ped']
    COMMA_SEPARATED_EXTENSIONS = ['.csv']

    def __init__(self, file_path) -> None:
        """Initialize an instance of the Loader class.

        Parameters: The path to the file.
        """
        try:
            assertion_message1 = 'The file path is not a string!'
            assertion_message2 = 'The file path was not found!'
            assertion_message3 = 'The file data is not valid!'

            assert isinstance(file_path, str), assertion_message1
            assert os.path.exists(file_path), assertion_message2

            self.__file_path = file_path
            self.__file_name = Path(file_path).name
            self.__file_stem = Path(file_path).stem
            self.__file_suffix = Path(file_path).suffix
            self.__file_data = self.read_file_data()

            assert self.validate_file_data(), assertion_message3
        except AssertionError as assertion_error:
            raise assertion_error

    @property
    def file_path(self) -> str:
        """Return the file path property of the class."""
        return self.__file_path

    @property
    def file_name(self) -> str:
        """Return the file name property of the class."""
        return self.__file_name

    @property
    def file_stem(self) -> str:
        """Return the file stem property of the class."""
        return self.__file_stem

    @property
    def file_suffix(self) -> str:
        """Return the file suffix property of the class."""
        return self.__file_suffix

    @property
    def file_data(self) -> list:
        """Return the file data property of the class."""
        return self.__file_data

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
        """Delete an instance of the Loader class."""
        del self.__file_path
        del self.__file_name
        del self.__file_stem
        del self.__file_suffix
        del self.__file_data

    @classmethod
    def manage_tab_separated(cls, file_object) -> dict:
        """Manage a separated file and return column order.

        Accepts: FILE_OBJECT of type TextIOWrapper
        Returns: DICT_OBJECT of type dict
        """
        try:
            assert isinstance(file_object, TextIOWrapper)
        except AssertionError as assertion_error:
            message = 'The file object is not valid!'
            raise AssertionError(message) from assertion_error

        dictionary_order = {}

        header_line = file_object.readline()
        header_line = re.sub(' +', '\t', header_line)
        header_line = re.sub('\t+', '\t', header_line)
        header_line = header_line.strip('\n').split('\t')

        for column_name in header_line:
            if column_name[1:] in Loader.PEDIGREE_COLUMNS:
                key_column = column_name[1:]
                dictionary_order[key_column] = header_line.index(column_name)
            else:
                message = 'The column name {} is not recognized'
                raise ValueError(message.format(column_name[1:]))

        return dictionary_order

    @classmethod
    def manage_comma_separated(cls, file_object) -> dict:
        """Manage a comma file and return column order.

        Accepts: FILE_OBJECT of type TextIOWrapper
        Returns: DICT_OBJECT of type dict
        """
        try:
            assert isinstance(file_object, TextIOWrapper)
        except AssertionError as assertion_error:
            message = 'The file object is not valid!'
            raise AssertionError(message) from assertion_error

        dictionary_order = {}
        csv_reader = csv.reader(file_object)

        try:
            header_line = [
                column for column in next(csv_reader) if column != ''
            ]
        except StopIteration as stop_iteration:
            message = 'The column iteration stopped!'
            raise StopIteration(message) from stop_iteration

        for column_name in header_line:
            if column_name in Loader.PEDIGREE_COLUMNS:
                dictionary_order[column_name] = header_line.index(column_name)
            else:
                message = 'The column name {} is not recognized'
                raise ValueError(message.format(column_name))

        return dictionary_order

    def read_file_data(self) -> list:
        """Read the file data from a given file.

        Accepts: No arguments.
        Returns: FILE_DATA of type list
        """
        file_data = []
        buffer_data = []

        with open(self.file_path, encoding='utf-8') as file:
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
                ordered_line = []

                for column_name in Loader.PEDIGREE_COLUMNS:
                    string_value = file_line[dictionary_order[column_name]]
                    ordered_line.append(string_value)

                file_data.append(ordered_line)

        return file_data


    def validate_file_data(self) -> bool:
        for data_unit in self.file_data:
            if data_unit[2] != '0':
                found_father = False
                for unit in self.file_data:
                    if data_unit[2] == unit[1]:
                        found_father = True

                if found_father is False:
                    return False

            if data_unit[3] != '0':
                found_mother = False
                for unit in self.file_data:
                    if data_unit[3] == unit[1]:
                        found_mother = True

                if found_mother is False:
                    return False

        return True


class Builder:
    """Class Name: Builder.

    This class is used to build every pedigree
    with its own individuals, mating units and
    sibship units inside by given file data.
    """

    def __init__(self, file_data) -> None:
        """Initialize an instance of the Builder class.

        Parameters: The file data from a file.
        """
        try:
            assert isinstance(file_data, list)
        except AssertionError as assertion_error:
            message = 'The constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__file_data = file_data
        self.__file_pedigrees = self.build_file_units()[0]
        self.__file_individuals = self.build_file_units()[1]

        self.build_inner_units()

    @property
    def file_data(self) -> list:
        """Return the file data property of the class."""
        return self.__file_data

    @property
    def file_pedigrees(self) -> list:
        """Return the file pedigrees property of the class."""
        return self.__file_pedigrees

    @property
    def file_individuals(self) -> list:
        """Return the file individuals property of the class."""
        return self.__file_individuals

    @file_data.deleter
    def file_data(self) -> None:
        del self.__file_data

    @file_pedigrees.deleter
    def file_pedigrees(self) -> None:
        del self.__file_pedigrees

    @file_individuals.deleter
    def file_individuals(self) -> None:
        del self.__file_individuals

    def __del__(self) -> None:
        """Delete an instance of the Loader class."""
        del self.__file_data
        del self.__file_pedigrees
        del self.__file_individuals

    def build_file_units(self) -> tuple:
        """Build file units by given data.

        Accepts: No arguments.
        Returns: PAIR of type tuple
        """
        file_pedigrees = []
        file_individuals = []

        for file_unit in self.file_data:
            if PedigreeFamily(file_unit[0]) not in file_pedigrees:
                file_pedigrees.append(PedigreeFamily(file_unit[0]))
            if Individual(file_unit) not in file_individuals:
                file_individuals.append(Individual(file_unit))

        return (file_pedigrees, file_individuals)

    def build_inner_units(self) -> None:
        """Build inner structure units from already built file units.

        Accepts: No arguments.
        Returns: No result.
        """
        for file_individual in self.file_individuals:
            assert isinstance(file_individual, Individual)

            for file_pedigree in self.file_pedigrees:
                assert isinstance(file_pedigree, PedigreeFamily)
                string1 = file_individual.pedigree_identifier
                string2 = file_pedigree.pedigree_identifier

                if string1 == string2:
                    file_pedigree.add_individual(file_individual)

        for file_pedigree in self.file_pedigrees:
            assert isinstance(file_pedigree, PedigreeFamily)
            file_pedigree.build_mating_units()
            file_pedigree.build_sibship_units()
            file_pedigree.build_generation_rank()
            file_pedigree.build_extended_sibship_units()
