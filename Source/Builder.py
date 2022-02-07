import sys
sys.path.append('..')

from FamilyUnits import Individual
from PedigreeFamily import PedigreeFamily


class Builder:
    def __init__(self, file_data) -> None:
        assert isinstance(file_data, list)

        self.__file_data        =   file_data
        self.__file_pedigrees   =   self.build_file_units()[0]
        self.__file_individuals =   self.build_file_units()[1]

        self.build_inner_units()


    @property
    def file_data(self) -> list:
        return self.__file_data


    @property
    def file_pedigrees(self) -> list:
        return self.__file_pedigrees


    @property
    def file_individuals(self) -> list:
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
        del self.__file_data
        del self.__file_pedigrees
        del self.__file_individuals


    def build_file_units(self) -> tuple:
        file_pedigrees      = list()
        file_individuals    = list()

        for file_unit in self.file_data:
            if PedigreeFamily(file_unit[0]) not in file_pedigrees:
                file_pedigrees.append(PedigreeFamily(file_unit[0]))
            if Individual(file_unit) not in file_individuals:
                file_individuals.append(Individual(file_unit))

        return (file_pedigrees, file_individuals)


    def build_inner_units(self) -> None:
        for file_individual in self.file_individuals:
            assert isinstance(file_individual, Individual)

            for file_pedigree in self.file_pedigrees:
                assert isinstance(file_pedigree, PedigreeFamily)
                if file_individual.pedigree_identifier == file_pedigree.pedigree_identifier:
                    file_pedigree.add_individual(file_individual)

        for file_pedigree in self.file_pedigrees:
            assert isinstance(file_pedigree, PedigreeFamily)
            file_pedigree.build_mating_units()
            file_pedigree.build_sibship_units()
            file_pedigree.build_generation_rank()
            file_pedigree.build_extended_sibship_units()
