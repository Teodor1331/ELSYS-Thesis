import sys

sys.path.append('..')


from FamilyUnits    import Individual
from PedigreeFamily import PedigreeFamily


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


    @file_data.setter
    def file_data(self, file_data):
        self.__file_data = file_data


    @file_pedigrees.setter
    def file_pedigrees(self, file_pedigrees):
        self.__file_pedigrees = file_pedigrees


    @file_individuals.setter
    def file_individuals(self, file_individuals):
        self.__file_individuals = file_individuals


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


loader = Loader('../../Examples/TXT Examples/Pedigree1.txt')
builder = Builder(loader.file_data)

for pedigree in builder.file_pedigrees:
    assert isinstance(pedigree, PedigreeFamily)
    print(pedigree.pedigree_identifier)
    print(pedigree.pedigree_individuals)
    print(pedigree.pedigree_mating_units)
    print(pedigree.pedigree_sibship_units)

    for individual in pedigree.pedigree_individuals:
        individual = pedigree.pedigree_individuals[individual]
        assert isinstance(individual, Individual)
        print(individual, individual.mating_unit_relation, individual.sibship_unit_relation)


    for mating_unit in pedigree.pedigree_mating_units:
        mating_unit = pedigree.pedigree_mating_units[mating_unit]
        print(mating_unit, mating_unit.male_mate_individual, mating_unit.female_mate_individual)


    for sibship_unit in pedigree.pedigree_sibship_units:
        sibship_unit = pedigree.pedigree_sibship_units[sibship_unit]
        print(sibship_unit, sibship_unit.siblings_individuals)
