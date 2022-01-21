import networkx as nx
import dynetworkx as dnx


from FamilyUnits    import Individual
from FamilyUnits    import MatingUnit
from FamilyUnits    import SibshipUnit
from PedigreeFamily import PedigreeFamily


class Interval():
    def __init__(self, left_element, right_element):
        self.__left_element     =   left_element
        self.__right_element    =   right_element


    @property
    def left_element(self):
        return self.__left_element


    @property
    def right_element(self):
        return self.__right_element


    def __del__(self):
        del self.__left_element
        del self.__right_element


    def find_intersection(self, interval):
        assert isinstance(interval, Interval)

        condition1 = self.right_element < interval.left_element
        condition2 = self.left_element > interval.right_element

        if condition1 or condition2:
            return None

        return Interval(
            max(self.left_element, interval.left_element),
            min(self.right_element, interval.right_element)
        )


class Graph:
    def __init__(self, pedigree_family):
        assert isinstance(pedigree_family, PedigreeFamily)
        
        self.__pedigree_family              =   pedigree_family
        self.__vertices_individuals         =   self.build_vertices_individuals()
        self.__vertices_mating_units        =   self.build_vertices_mating_units()
        self.__vertices_sibship_units       =   self.build_vertices_sibship_units()
        self.__vertices_pedigree_union      =   self.build_vertices_pedigree_union()
        self.__vertices_generation_ranks    =   set()
        self.__graph_instance               =   self.build_pedigree_graph()

        self.remove_edges_by_rules()

        self.__graph_instance = self.graph_instance.to_undirected()


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
        vertices_individuals = list()

        for key in self.pedigree_family.pedigree_individuals:
            individual = self.pedigree_family.pedigree_individuals[key]
            assert isinstance(individual, Individual)
            vertices_individuals.append(individual)

        return vertices_individuals


    def build_vertices_mating_units(self):
        vertices_mating_units = list()

        for key in self.pedigree_family.pedigree_mating_units:
            mating_unit = self.pedigree_family.pedigree_mating_units[key]
            assert isinstance(mating_unit, MatingUnit)
            vertices_mating_units.append(mating_unit)

        return vertices_mating_units


    def build_vertices_sibship_units(self):
        vertices_sibship_units = list()

        for key in self.pedigree_family.pedigree_sibship_units:
            sibship_unit = self.pedigree_family.pedigree_sibship_units[key]
            assert isinstance(sibship_unit, SibshipUnit)
            vertices_sibship_units.append(sibship_unit)

        return vertices_sibship_units


    def build_vertices_pedigree_union(self):
        vertices_pedigree_union = list()
        vertices_pedigree_union += list(self.vertices_individuals)
        vertices_pedigree_union += list(self.vertices_mating_units)
        vertices_pedigree_union += list(self.vertices_sibship_units)
        return vertices_pedigree_union


    def build_pedigree_graph(self):
        graph_instance = nx.DiGraph()

        graph_instance.add_nodes_from(self.vertices_individuals)
        graph_instance.add_nodes_from(self.vertices_mating_units)
        graph_instance.add_nodes_from(self.vertices_sibship_units)

        for current_individual in self.vertices_individuals:
            assert isinstance(current_individual, Individual)

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)
                graph_instance.add_edge(current_individual, individual)

            for mating_unit in self.vertices_mating_units:
                assert isinstance(mating_unit, MatingUnit)
                graph_instance.add_edge(current_individual, mating_unit)

            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(sibship_unit, SibshipUnit)
                graph_instance.add_edge(current_individual, sibship_unit)

        for current_mating_unit in self.vertices_mating_units:
            assert isinstance(current_mating_unit, MatingUnit)

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)
                graph_instance.add_edge(current_mating_unit, individual)

            for mating_unit in self.vertices_mating_units:
                assert isinstance(mating_unit, MatingUnit)
                graph_instance.add_edge(current_mating_unit, mating_unit)

            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(sibship_unit, SibshipUnit)
                graph_instance.add_edge(current_mating_unit, sibship_unit)

        for current_sibship_unit in self.vertices_sibship_units:
            assert isinstance(sibship_unit, SibshipUnit)

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)
                graph_instance.add_edge(current_sibship_unit, individual)

            for mating_unit in self.vertices_mating_units:
                assert isinstance(mating_unit, MatingUnit)
                graph_instance.add_edge(current_sibship_unit, mating_unit)

            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(sibship_unit, SibshipUnit)
                graph_instance.add_edge(current_sibship_unit, sibship_unit)

        return graph_instance


    def build_sets_from_individual(self, individual):
        assert isinstance(individual, Individual)

        pedigree_vertices   =   set()
        generation_vertices =   set()
        children_vertices   =   set()

        return (pedigree_vertices, generation_vertices, children_vertices)


    def build_sets_from_mating_unit(self, mating_unit):
        assert isinstance(mating_unit, MatingUnit)

        pedigree_vertices   =   set()
        generation_vertices =   set()
        children_vertices   =   set()

        return (pedigree_vertices, generation_vertices, children_vertices)


    def build_sets_from_sibship_unit(self, sibship_unit):
        assert isinstance(sibship_unit, SibshipUnit)

        pedigree_vertices       =   set()
        generation_vertices     =   set()
        children_vertices       =   set()

        print(pedigree_vertices, generation_vertices, children_vertices)


    def find_edges_rule_a(self):
        edges_minus     =   list()

        start_index = self.pedigree_family.min_generation_rank
        final_index = self.pedigree_family.max_generation_rank

        for i in range(start_index, final_index + 1):
            current_individuals = self.pedigree_family.get_individuals_by_generation(i)

            for n in range(len(current_individuals)):
                for m in range(len(current_individuals)):
                    edges_minus.append((current_individuals[n], current_individuals[m]))

        return edges_minus


    def find_edges_rule_b(self):
        edges_minus     =   list()
        edges_plus      =   list()

        for mating_unit in self.vertices_mating_units:
            assert isinstance(mating_unit, MatingUnit)

            male_mate = mating_unit.male_mate_individual
            female_mate = mating_unit.female_mate_individual

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)

                condition1 = individual is not male_mate
                condition2 = individual is not female_mate
                condition3 = individual.generation_rank == mating_unit.generation_rank

                if condition1 and condition2 and condition3:
                    edges_minus.append((mating_unit, individual))
                    edges_minus.append((individual, mating_unit))

                


        for mating_unit in self.vertices_mating_units:
            assert isinstance(mating_unit, MatingUnit)

            male_mate = mating_unit.male_mate_individual
            female_mate = mating_unit.female_mate_individual

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)

                condition1 = individual is male_mate
                condition2 = individual is female_mate

                if condition1 or condition2:
                    edges_plus.append((mating_unit, individual))
                    edges_plus.append((individual, mating_unit))

        return (edges_minus, edges_plus)


    def find_edges_rule_c(self):
        edges_minus     =   list()
        edges_plus      =   list()

        for sibship_unit in self.vertices_sibship_units:
            assert isinstance(sibship_unit, SibshipUnit)

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)
                condition1 = individual not in sibship_unit.siblings_individuals
                condition2 = individual.generation_rank == sibship_unit.generation_rank

                if condition1 and condition2:
                    edges_minus.append((individual, sibship_unit))
                    edges_minus.append((sibship_unit, individual))

        for sibship_unit in self.vertices_sibship_units:
            assert isinstance(sibship_unit, SibshipUnit)

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)

                if individual in sibship_unit.siblings_individuals:
                    edges_plus.append((individual, sibship_unit))
                    edges_plus.append((sibship_unit, individual))

        return (edges_minus, edges_plus)


    def find_edges_rule_d(self):
        edges_plus      =   list()

        for mating_unit in self.vertices_mating_units:
            assert isinstance(mating_unit, MatingUnit)

            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(sibship_unit, SibshipUnit)

                if mating_unit.sibship_unit_relation is sibship_unit:
                    edges_plus.append((mating_unit, sibship_unit))
                    edges_plus.append((sibship_unit, mating_unit))

        return edges_plus


    def find_edges_rule_e(self):
        edges_minus     =   list()

        for mating_unit in self.vertices_mating_units:
            assert isinstance(mating_unit, MatingUnit)

            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(sibship_unit, SibshipUnit)

                if mating_unit.sibship_unit_relation is not sibship_unit:
                    edges_minus.append((mating_unit, sibship_unit))
                    edges_minus.append((sibship_unit, mating_unit))

        return edges_minus


    def remove_edges_by_rules(self):
        self.__graph_instance.remove_edges_from(self.find_edges_rule_a())
        self.__graph_instance.remove_edges_from(self.find_edges_rule_b()[0])
        self.__graph_instance.remove_edges_from(self.find_edges_rule_c()[0])
        self.__graph_instance.remove_edges_from(self.find_edges_rule_e())


    def validate_edges_by_rules(self):
        for edge in self.find_edges_rule_b()[1]:
            if edge not in self.graph_instance.edges():
                return False

        for edge in self.find_edges_rule_c()[1]:
            if edge not in self.graph_instance.edges():
                return False

        for edge in self.find_edges_rule_d():
            if edge not in self.graph_instance.edges():
                return False

        return True
