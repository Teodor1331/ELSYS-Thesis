from FamilyUnits    import Individual
from PedigreeFamily import PedigreeFamily


class Validator:
    def __init__(self, pedigree_family):
        assert isinstance(pedigree_family, PedigreeFamily)
        self.__pedigree_family      =   pedigree_family
        self.__condition_matings    =   self.validate_condition_matings()
        self.__condition_cycles     =   self.validate_condition_cycles()


    @property
    def pedigree_family(self):
        return self.__pedigree_family


    def __del__(self):
        del self.__pedigree_family
        del self.__condition_matings
        del self.__condition_cycles


    def validate_condition_matings(self):
        for key in self.pedigree_family.pedigree_individuals:
            individual = self.pedigree_family.pedigree_individuals[key]
            assert isinstance(individual, Individual)

            if individual.number_matings > 2:
                return False

        return True


    def validate_condition_cycles(self):
        pass
