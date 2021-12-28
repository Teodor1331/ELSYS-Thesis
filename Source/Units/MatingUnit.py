from .Individual import Individual


class MatingUnit:
    def __init__(self, pedigree_identifier, male_mate_individual, female_mate_individual, sibship_unit_relation):
        assert isinstance(pedigree_identifier,      str)
        assert isinstance(male_mate_individual,     Individual)
        assert isinstance(female_mate_individual,   Individual)
        #assert isinstance(sibship_unit_relation,    (SibshipUnit, type(None)))
        
        self.__pedigree_identifier      =   pedigree_identifier
        self.__male_mate_individual     =   male_mate_individual
        self.__female_mate_individual   =   female_mate_individual
        self.__sibship_unit_relation    =   sibship_unit_relation
        self.__generation_rank          =   None


    @property
    def pedigree_identifier(self):
        return self.__pedigree_identifier


    @property
    def male_mate_individual(self):
        return self.__male_mate_individual


    @property
    def female_mate_individual(self):
        return self.__female_mate_individual


    @property
    def sibship_unit_relation(self):
        return self.__sibship_unit_relation


    @property
    def generation_rank(self):
        return self.__generation_rank


    @pedigree_identifier.setter
    def pedigree_identifier(self, pedigree_identifier):
        self.__pedigree_identifier = pedigree_identifier


    @male_mate_individual.setter
    def male_mate_individual(self, male_mate_individual):
        self.__male_mate_individual = male_mate_individual


    @female_mate_individual.setter
    def female_mate_individual(self, female_mate_individual):
        self.__female_mate_individual = female_mate_individual


    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation):
        self.__sibship_unit_relation = sibship_unit_relation


    @pedigree_identifier.deleter
    def pedigree_identifier(self):
        del self.__pedigree_identifier


    @male_mate_individual.deleter
    def male_mate_individual(self):
        del self.__male_mate_individual


    @female_mate_individual.deleter
    def female_mate_individual(self):
        del self.__female_mate_individual


    @sibship_unit_relation.deleter
    def sibship_unit_relation(self):
        del self.__sibship_unit_relation


    def __hash__(self):
        return  hash(self.male_mate_individual) + \
                hash(self.female_mate_individual)


    def __eq__(self, mating_unit):
        assert isinstance(mating_unit, (MatingUnit, type(None)))
        return self.__hash__() == mating_unit.__hash__()


    def __repr__(self):
        return "MU-" + self.mating_string()


    def __del__(self):
        del self.__pedigree_identifier
        del self.__male_mate_individual
        del self.__female_mate_individual
        del self.__sibship_unit_relation
        del self.__generation_rank


    def mating_string(self):
        return  str(self.male_mate_individual) + \
                str(self.female_mate_individual)


    def set_generation_rank(self, generation_rank):
        self.__generation_rank = generation_rank
