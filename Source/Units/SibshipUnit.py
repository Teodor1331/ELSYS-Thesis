try:
    from .Individual import Individual
    from .MatingUnit import MatingUnit
except ImportError:
    pass


class SibshipUnit:
    def __init__(self, pedigree_identifier, mating_unit_relation):
        assert isinstance(pedigree_identifier,  str)
        assert isinstance(mating_unit_relation, MatingUnit)

        self.__pedigree_identifier      =   pedigree_identifier
        self.__siblings_individuals     =   dict()
        self.__mating_unit_relation     =   mating_unit_relation
        self.__generation_rank          =   None


    @property
    def pedigree_identifier(self):
        return self.__pedigree_identifier


    @property
    def siblings_individuals(self):
        return self.__siblings_individuals


    @property
    def mating_unit_relation(self):
        return self.__mating_unit_relation


    @property
    def generation_rank(self):
        return self.__generation_rank


    @pedigree_identifier.deleter
    def pedigree_identifier(self):
        del self.__pedigree_identifier


    @siblings_individuals.deleter
    def siblings_individuals(self):
        del self.__siblings_individuals


    @mating_unit_relation.deleter
    def mating_unit_relation(self):
        del self.__mating_unit_relation


    @generation_rank.deleter
    def generation_rank(self):
        del self.__generation_rank


    def __hash__(self):
        return hash(self.mating_unit_relation)


    def __eq__(self, sibship_unit):
        assert isinstance(sibship_unit, SibshipUnit)
        return self.__hash__() == sibship_unit.__hash__()


    def __repr__(self):
        return "SU-" + self.mating_unit_relation.mating_string()


    def __del__(self):
        del self.__pedigree_identifier
        del self.__siblings_individuals
        del self.__mating_unit_relation
        del self.__generation_rank


    def add_sibling_individual(self, sibling_individual):
        assert isinstance(sibling_individual, Individual)
        key = "Child-" + len(self.siblings_individuals)
        self.__siblings_individuals[key] = sibling_individual
