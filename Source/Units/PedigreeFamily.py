from .Individual    import Individual
from .MatingUnit    import MatingUnit
from .SibshipUnit   import SibshipUnit


class PedigreeFamily:
    def __init__(self, pedigree_identifier):
        self.__pedigree_identifier      =   pedigree_identifier
        self.__pedigree_individuals     =   dict()
        self.__pedigree_mating_units    =   dict()
        self.__pedigree_sibship_units   =   dict()


    @property
    def pedigree_identifier(self):
        return self.__pedigree_identifier


    @property
    def pedigree_individuals(self):
        return self.__pedigree_individuals


    @property
    def pedigree_mating_units(self):
        return self.__pedigree_mating_units


    @property
    def pedigree_sibship_units(self):
        return self.__pedigree_sibship_units


    @pedigree_identifier.deleter
    def pedigree_identifier(self):
        del self.__pedigree_identifier


    @pedigree_individuals.deleter
    def pedigree_individuals(self):
        del self.__pedigree_individuals

    
    @pedigree_mating_units.deleter
    def pedigree_mating_units(self):
        del self.__pedigree_mating_units


    @pedigree_sibship_units.deleter
    def pedigree_sibship_units(self):
        del self.__pedigree_sibship_units


    def __hash__(self):
        return hash(self.pedigree_identifier)


    def __eq__(self, pedigree_family):
        assert isinstance(pedigree_family, PedigreeFamily)
        return self.__hash__() == pedigree_family.__hash__()


    def __repr__(self):
        return self.pedigree_identifier


    def __del__(self):
        del self.__pedigree_identifier
        del self.__pedigree_individuals
        del self.__pedigree_mating_units
        del self.__pedigree_sibship_units


    def add_individual(self, individual):
        assert isinstance(individual, Individual)
        key = individual.individual_identifier
        self.__pedigree_individuals[key] = individual


    def add_mating_unit(self, mating_unit):
        assert isinstance(mating_unit, MatingUnit)
        key = mating_unit.__repr__
        self.__pedigree_mating_units[key] = mating_unit


    def add_sibship_unit(self, sibship_unit):
        assert isinstance(sibship_unit, SibshipUnit)
        key = sibship_unit.__repr__
        self.__pedigree_sibship_units[key] = sibship_unit


    def build_mating_units(self):
        for individual in self.pedigree_individuals:
            current_individual = self.pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)

            if current_individual.individual_father != '0' and current_individual.individual_mother != '0':
                father = self.pedigree_individuals[current_individual.individual_father]
                mother = self.pedigree_individuals[current_individual.individual_mother]

                current_mating_unit = MatingUnit(self.pedigree_identifier, father, mother, None)
                current_sibship_unit = SibshipUnit(self.pedigree_identifier, current_mating_unit)
                current_mating_unit = MatingUnit(self.pedigree_identifier, father, mother, current_sibship_unit)

                self.pedigree_mating_units[str(current_mating_unit)]    = current_mating_unit
                self.pedigree_sibship_units[str(current_sibship_unit)]  = current_sibship_unit

                current_individual.set_mating_unit_relation(self.pedigree_mating_units[str(current_mating_unit)])
                current_individual.set_sibship_unit_relation(self.pedigree_sibship_units[str(current_mating_unit.sibship_unit_relation)])


    def build_sibship_units(self):
        for sibship_unit in self.pedigree_sibship_units:
            current_sibship_unit = self.pedigree_sibship_units[sibship_unit]
            assert isinstance(current_sibship_unit, SibshipUnit)

            for individual in self.pedigree_individuals:
                current_individual = self.pedigree_individuals[individual]
                assert isinstance(current_individual, Individual)

                if current_individual.sibship_unit_relation != None:
                    if current_individual.sibship_unit_relation == current_sibship_unit:
                        current_sibship_unit.add_sibling_individual(current_individual)
                        current_individual.set_sibship_unit_relation(current_sibship_unit)

