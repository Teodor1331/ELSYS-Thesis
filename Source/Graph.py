import networkx as nx


from FamilyUnits    import Individual
from FamilyUnits    import MatingUnit
from FamilyUnits    import SibshipUnit
from PedigreeFamily import PedigreeFamily


class Graph:
    def __init__(self, pedigree_family):
        assert isinstance(pedigree_family, PedigreeFamily)
        
        self.__pedigree_family              =   pedigree_family
        self.__vertices_individuals         =   self.build_vertices_individuals()
        self.__vertices_mating_units        =   self.build_vertices_mating_units()
        self.__vertices_sibship_units       =   self.build_vertices_sibship_units()
        self.__vertices_pedigree_union      =   self.build_vertices_pedigree_union()
        self.__vertices_generation_ranks    =   set()
        self.__graph_instance               =   nx.Graph()


    @property
    def pedigree_family(self):
        return self.__pedigree_family


    @property
    def vertices_individuals(self):
        return self.__vertices_individuals


    @property
    def vertices_mating_units(self):
        return self.__vertices_mating_units


    @property
    def vertices_sibship_units(self):
        return self.__vertices_sibship_units


    @property
    def vertices_pedigree_union(self):
        return self.__vertices_pedigree_union


    @property
    def vertices_generation_ranks(self):
        return self.__vertices_generation_ranks


    @property
    def graph_instance(self):
        return self.__graph_instance


    @pedigree_family.setter
    def pedigree_family(self, pedigree_family):
        self.__pedigree_family = pedigree_family


    @vertices_individuals.setter
    def vertices_individuals(self, vertices_individuals):
        self.__vertices_individuals = vertices_individuals


    @vertices_mating_units.setter
    def vertices_mating_units(self, vertices_mating_units):
        self.__vertices_mating_units = vertices_mating_units


    @vertices_sibship_units.setter
    def vertices_sibship_units(self, vertices_sibship_units):
        self.__vertices_sibship_units = vertices_sibship_units


    @vertices_pedigree_union.setter
    def vertices_pedigree_union(self, vertices_pedigree_union):
        self.__vertices_pedigree_union = vertices_pedigree_union


    @vertices_generation_ranks.setter
    def vertices_generation_ranks(self, vertices_generation_ranks):
        self.__vertices_generation_ranks = vertices_generation_ranks


    @graph_instance.setter
    def graph_instance(self, graph_instance):
        self.__graph_instance = graph_instance


    @pedigree_family.deleter
    def pedigree_family(self):
        del self.__pedigree_family


    @vertices_individuals.deleter
    def vertices_individuals(self):
        del self.__vertices_individuals


    @vertices_mating_units.deleter
    def vertices_mating_units(self):
        del self.__vertices_mating_units


    @vertices_sibship_units.deleter
    def vertices_sibship_units(self):
        del self.__vertices_sibship_units


    @vertices_pedigree_union.deleter
    def vertices_pedigree_union(self):
        del self.__vertices_pedigree_union


    @vertices_generation_ranks.deleter
    def vertices_generation_ranks(self):
        del self.__vertices_generation_ranks


    @graph_instance.deleter
    def graph_instance(self):
        del self.__graph_instance

    
    def __del__(self):
        del self.__pedigree_family
        del self.__vertices_individuals
        del self.__vertices_mating_units
        del self.__vertices_sibship_units
        del self.__vertices_pedigree_union
        del self.__vertices_generation_ranks
        del self.__graph_instance


    def build_vertices_individuals(self):
        vertices_individuals = set()

        for key in self.pedigree_family.pedigree_individuals:
            individual = self.pedigree_family.pedigree_individuals[key]
            assert isinstance(individual, Individual)
            vertices_individuals.add(individual)

        return vertices_individuals


    def build_vertices_mating_units(self):
        vertices_mating_units = set()

        for key in self.pedigree_family.pedigree_mating_units:
            mating_unit = self.pedigree_family.pedigree_mating_units[key]
            assert isinstance(mating_unit, MatingUnit)
            vertices_mating_units.add(mating_unit)

        return vertices_mating_units


    def build_vertices_sibship_units(self):
        vertices_sibship_units = set()

        for key in self.pedigree_family.pedigree_sibship_units:
            sibship_unit = self.pedigree_family.pedigree_sibship_units[key]
            assert isinstance(sibship_unit, SibshipUnit)
            vertices_sibship_units.add(sibship_unit)

        return vertices_sibship_units


    def build_vertices_pedigree_union(self):
        vertices_pedigree_union = set()
        vertices_pedigree_union.union(self.vertices_individuals)
        vertices_pedigree_union.union(self.vertices_mating_units)
        vertices_pedigree_union.union(self.vertices_sibship_units)
        return vertices_pedigree_union
