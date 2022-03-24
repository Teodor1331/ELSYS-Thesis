# This Python file uses the following encoding: UTF-8

"""The module has the classes Loader and Builder.

This module contains the logic of reading a pedigree file
and building pedigree nuclear families with pedigree units.
"""

from pathlib import Path
from typing import TextIO
from io import TextIOWrapper
from collections import defaultdict

import os
import sys
import re
import csv

from .pedigree_units import Individual
from .pedigree_family import PedigreeFamily


class Loader:
    """Class Name: Loader.

    This class is used to load the whole
    data from a pedigree file. The file
    can be tabbed separated or comma separated.
    By default, the file is in PED format.
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

    def __init__(self, file_path: str) -> None:
        """Initialize an instance of the Loader class.

        Parameters: The path to the file with the data.
        """
        try:
            not_string_message = 'The file path is not a string!'
            not_found_message = 'The file path was not found!'
            not_file_message = 'The file has invalid format!'
            not_access_message = 'The file is not accessible!'
            not_valid_message = 'The file data is not valid!'

            assert isinstance(file_path, str), not_string_message
            assert os.path.exists(file_path), not_found_message

            assert os.path.isfile(file_path), not_file_message
            assert os.access(file_path, os.R_OK), not_access_message

            self.__file_path = file_path
            self.__file_name = Path(file_path).name
            self.__file_stem = Path(file_path).stem
            self.__file_suffix = Path(file_path).suffix
            self.__file_data = self.read_file_data()

            assert self.validate_file_data(), not_valid_message
        except AssertionError as assertion_error:
            print(str(assertion_error))
            print("Check the data in your file!")
            sys.exit(1)
        except ValueError as value_error:
            print(str(value_error))
            print("Check the data in your file!")
            sys.exit(2)
        except StopIteration as stop_iteration:
            print(str(stop_iteration))
            print("Check the data in your file!")
            sys.exit(3)

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

    @classmethod
    def manage_tabbed_separated(cls, file_object: TextIO) -> dict:
        """Manage a tabbed separated file and return column order.

        This method accepts a file object and returns a dictionary
        with the order of the columns in the file as they are.
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
                message = 'The column name {} is not recognized!'
                raise ValueError(message.format(column_name[1:]))

        if len(dictionary_order) != len(Loader.PEDIGREE_COLUMNS):
            message = 'There is a missing column in the file!'
            raise ValueError(message)

        return dictionary_order

    @classmethod
    def manage_comma_separated(cls, file_object: TextIO) -> dict:
        """Manage a comma separated file and return column order.

        This method accepts a file object and returns a dictionary
        with the order of the columns in the file as they are.
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
                message = 'The column name {} is not recognized!'
                raise ValueError(message.format(column_name))

        if len(dictionary_order) != len(Loader.PEDIGREE_COLUMNS):
            message = 'There is a missing column in the file!'
            raise ValueError(message)

        return dictionary_order

    def read_file_data(self) -> list:
        """Read the file data from a given file.

        This method manages the whole reading of the file,
        no matter if it is tabbed or comma separated.
        """
        file_data = []
        buffer_data = []

        with open(self.file_path, encoding='utf-8') as file:
            if self.file_suffix.lower() in Loader.TAB_SEPARATED_EXTENSIONS:
                dictionary_order = self.manage_tabbed_separated(file)

                filelines = file.readlines()

                if len(filelines) != 1 and filelines[-1] != '\n':
                    raise ValueError('The file must end with a new line!')

                for file_line in filelines[:-1]:
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
        """Validate the file data from a given file."""
        distributed_data = defaultdict(list)

        for data_unit in self.file_data:
            distributed_data[data_unit[0]].append(data_unit)

        for key in distributed_data:
            data = distributed_data[key]

            if not Loader.validate_number_individuals(data):
                return False

            if not Loader.validate_context_individuals(data):
                return False

            if not Loader.validate_individual_parents(data):
                return False

            if not Loader.find_proband_individual(data):
                return False

        return True

    @staticmethod
    def validate_number_individuals(data: list) -> bool:
        """Validate the number of the individuals in a file.

        This methods checks if the number of the individuals
        in the file is exactly less than 3 or not.
        """
        return not len(data) < 3

    @staticmethod
    def validate_context_individuals(data: list) -> bool:
        """Validate the context of the individuals in a file.

        This method checks if every individual in the file has
        its own father and mother in the same file data.
        """
        for data_unit in data:
            found_father = Loader.find_parent_individual(data, data_unit, 2)
            found_mother = Loader.find_parent_individual(data, data_unit, 3)

            if not found_mother or not found_father:
                return False

        return True

    @staticmethod
    def validate_individual_parents(data: list) -> bool:
        """Validate the gender of the parents of an individual.

        This methods validates the gender of the parents of
        every single individual. For example, if the individual
        is not a product of two mothers or two fathers.
        """
        for unit in data:
            validated_father = True
            validated_mother = True

            if unit[2] != '0':
                for data_unit in data:
                    if data_unit[1] == unit[2]:
                        validated_father = data_unit[4] == '1'
                        break

            if unit[3] != '0':
                for data_unit in data:
                    if data_unit[1] == unit[3]:
                        validated_mother = data_unit[4] == '2'
                        break

            if not validated_father or not validated_mother:
                return False

        return True

    @staticmethod
    def find_parent_individual(data: list,
                               data_unit: list, index: int) -> bool:
        """Find a parent of the individual in the file.

        This methods looks for the parent individual of a
        current one on the read file data of the same file.
        """
        if data_unit[index] == '0':
            return True

        for unit in data:
            if data_unit[index] == unit[1]:
                return True

        return False

    @staticmethod
    def find_proband_individual(data: list) -> bool:
        """Find a single proband individual in the file.

        This method looks for the proband individual in
        the whole file data of the pedigree.
        """
        return len([1 for data_unit in data
                    if data_unit[6] == 'prb'
                    ]) == 1


class Builder:
    """Class Name: Builder.

    This class is used to build every pedigree
    with its own individuals, mating units and
    sibship units inside by given file data.
    """

    def __init__(self, file_data: list) -> None:
        """Initialize an instance of the Builder class.

        Parameters: The file data from a file.
        """
        try:
            assert isinstance(file_data, list)
        except AssertionError as assertion_error:
            print(str(assertion_error))
            print("Invalid file data!")
            sys.exit(4)

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

    def build_file_units(self) -> tuple:
        """Build file units by given data.

        This method build the units which comes
        directly from the file data. These units
        are the individuals and the pedigree
        (without its internal structure).
        """
        file_pedigrees = []
        file_individuals = []

        for file_unit in self.file_data:
            if PedigreeFamily(file_unit[0]) not in file_pedigrees:
                file_pedigrees.append(PedigreeFamily(file_unit[0]))
            if Individual(file_unit) not in file_individuals:
                file_individuals.append(Individual(file_unit))

        return file_pedigrees, file_individuals

    def build_inner_units(self) -> None:
        """Build inner structure units from already built file units.

        This method builds the whole structure of a pedigree by
        distributing the individuals to their corresponding pedigrees
        and calling the needed methods in every single pedigree for
        building the hierarchy and the organization of the base units.
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
            file_pedigree.collect_mating_units_for_individuals()
