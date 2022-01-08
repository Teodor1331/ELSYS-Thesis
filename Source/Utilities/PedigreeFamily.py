from FamilyUnits import Individual
from FamilyUnits import MatingUnit
from FamilyUnits import SibshipUnit


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


    @pedigree_identifier.setter
    def pedigree_identifier(self, pedigree_identifier):
        self.__pedigree_identifier = pedigree_identifier


    @pedigree_individuals.setter
    def pedigree_individuals(self, pedigree_individuals):
        self.__pedigree_individuals = pedigree_individuals


    @pedigree_mating_units.setter
    def pedigree_mating_units(self, pedigree_mating_units):
        self.__pedigree_mating_units = pedigree_mating_units


    @pedigree_sibship_units.setter
    def pedigree_sibship_units(self, pedigree_sibship_units):
        self.__pedigree_sibship_units = pedigree_sibship_units


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

                current_individual.mating_unit_relation     = self.pedigree_mating_units[str(current_mating_unit)]
                current_individual.sibship_unit_relation    = self.pedigree_sibship_units[str(current_mating_unit.sibship_unit_relation)]


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
                        current_individual.sibship_unit_relation = current_sibship_unit


    def get_proband_data(self):
        proband                     =   None
        proband_generation_rank     =   None
        proband_mating_unit         =   None
        proband_sibship_unit        =   None


        for individual in self.pedigree_individuals:
            current_individual = self.pedigree_individuals[individual]
            assert isinstance(current_individual, Individual)

            if current_individual.individual_role == 'prb':
                current_individual.generation_rank = 0
                proband                 = current_individual
                proband_generation_rank = current_individual.generation_rank
                break


        for sibship_unit in self.pedigree_sibship_units:
            current_sibship_unit = self.pedigree_sibship_units[sibship_unit]
            assert isinstance(current_sibship_unit, SibshipUnit)

            if proband.sibship_unit_relation == current_sibship_unit:
                proband_sibship_unit = current_sibship_unit


        for mating_unit in self.pedigree_mating_units:
            current_mating_unit = self.pedigree_mating_units[mating_unit]
            assert isinstance(current_mating_unit, MatingUnit)

            if proband.mating_unit_relation == current_mating_unit:
                proband_mating_unit = current_mating_unit


        return [proband, proband_generation_rank, proband_mating_unit, proband_sibship_unit]


    def build_generation_rank(self):
        proband_data = self.get_proband_data()

        assert isinstance(proband_data[0], Individual)
        assert isinstance(proband_data[1], int)

        touched_individuals = []

        for sibship_unit in self.pedigree_sibship_units:
            current_sibship_unit = self.pedigree_sibship_units[sibship_unit]
            assert isinstance(current_sibship_unit, SibshipUnit)

            if proband_data[0].sibship_unit_relation == current_sibship_unit:
                for i in range(len(current_sibship_unit.siblings_individuals)):
                    sibling = current_sibship_unit.siblings_individuals[i]
                    assert isinstance(sibling, Individual)
                    sibling.generation_rank = proband_data[1]
                    touched_individuals.append(sibling)
                    current_sibship_unit.change_sibling_individual(sibling, i)

        for mating_unit in self.pedigree_mating_units:
            current_mating_unit = self.pedigree_mating_units[mating_unit]
            assert isinstance(current_mating_unit, MatingUnit)

            if proband_data[0].mating_unit_relation == current_mating_unit:
                current_mating_unit.male_mate_individual.generation_rank    = proband_data[1] - 1
                current_mating_unit.female_mate_individual.generation_rank  = proband_data[1] - 1
                touched_individuals.append(sibling)


        for mating_unit in self.pedigree_mating_units:
            current_mating_unit = self.pedigree_mating_units[mating_unit]
            assert isinstance(current_mating_unit, MatingUnit)

            if  proband_data[0] == current_mating_unit.male_mate_individual or \
                proband_data[0] == current_mating_unit.female_mate_individual:
                assert isinstance(current_mating_unit.sibship_unit_relation, SibshipUnit)

                for i in range(len(current_mating_unit.sibship_unit_relation.siblings_individuals)):
                    sibling = current_mating_unit.sibship_unit_relation.siblings_individuals[i]
                    assert isinstance(sibling, Individual)
                    sibling.generation_rank = proband_data[1] + 1
                    current_mating_unit.sibship_unit_relation.change_sibling_individual(sibling, i)


        for mating_unit in self.pedigree_mating_units:
            current_mating_unit = self.pedigree_mating_units[mating_unit]
            assert isinstance(current_mating_unit, MatingUnit)

            if proband_data[0] == current_mating_unit.male_mate_individual:
                current_mating_unit.female_mate_individual.generation_rank = proband_data[1]
            elif proband_data[0] == current_mating_unit.female_mate_individual:
                current_mating_unit.male_mate_individual.generation_rank = proband_data[1]