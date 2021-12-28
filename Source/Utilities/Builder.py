import sys

sys.path.append('..')


from Units.Individual       import Individual
from Units.PedigreeFamily   import PedigreeFamily


from Loader import Loader


class Builder:
    def __init__(self, file_data):
        assert isinstance(file_data, list)

        self.__file_data        =   file_data
        self.__file_pedigrees   =   self.build_file_units()[0]
        self.__file_individuals =   self.build_file_units()[1]

        self.build_inner_units()


    @property
    def file_data(self):
        return self.__file_data


    @property
    def file_pedigrees(self):
        return self.__file_pedigrees


    @property
    def file_individuals(self):
        return self.__file_individuals


    @file_data.deleter
    def file_data(self):
        del self.__file_data


    @file_pedigrees.deleter
    def file_pedigrees(self):
        del self.__file_pedigrees


    @file_individuals.deleter
    def file_individuals(self):
        del self.__file_individuals


    def __del__(self):
        del self.__file_data
        del self.__file_pedigrees
        del self.__file_individuals


    def build_file_units(self):
        file_pedigrees      = list()
        file_individuals    = list()

        for file_unit in self.file_data:
            if PedigreeFamily(file_unit[0]) not in file_pedigrees:
                file_pedigrees.append(PedigreeFamily(file_unit[0]))
            if Individual(file_unit) not in file_individuals:
                file_individuals.append(Individual(file_unit))

        return (file_pedigrees, file_individuals)


    def build_inner_units(self):
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
