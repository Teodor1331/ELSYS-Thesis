import networkx as nx


class Graph:
    def __init__(self, pedigree_family):
        self.__pedigree_family              =   pedigree_family
        self.__vertices_individuals         =   set()
        self.__vertices_mating_units        =   set()
        self.__vertices_sibship_units       =   set()
        self.__vertices_pedigree_union      =   set()
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
