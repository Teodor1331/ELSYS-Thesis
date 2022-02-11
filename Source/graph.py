import networkx as nx
import dynetworkx as dnx

from ordered_set import OrderedSet
from collections import deque


from family_units import Individual
from family_units import MatingUnit
from family_units import SibshipUnit
from pedigree_family import PedigreeFamily
from interval_sandwich import Interval
from interval_sandwich import CutRealization


class Graph:
    def __init__(self, pedigree_family):
        try:
            assert isinstance(pedigree_family, PedigreeFamily)
        except AssertionError:
            raise AssertionError('The graph constructor arguments are not correct!')
        
        self.__pedigree_family              =   pedigree_family
        self.__vertices_individuals         =   self.build_vertices_individuals()
        self.__vertices_mating_units        =   self.build_vertices_mating_units()
        self.__vertices_sibship_units       =   self.build_vertices_sibship_units()
        self.__vertices_pedigree_union      =   self.build_vertices_pedigree_union()

        self.__graph_instance               =   self.build_pedigree_graph()
        self.__mandatory_graph              =   self.build_mandatory_graph()
        self.__forbidden_graph              =   self.build_forbidden_graph()


    @property
    def pedigree_family(self) -> PedigreeFamily:
        return self.__pedigree_family


    @property
    def vertices_individuals(self) -> list:
        return self.__vertices_individuals


    @property
    def vertices_mating_units(self) -> list:
        return self.__vertices_mating_units


    @property
    def vertices_sibship_units(self) -> list:
        return self.__vertices_sibship_units


    @property
    def vertices_pedigree_union(self) -> OrderedSet:
        return self.__vertices_pedigree_union


    @property
    def graph_instance(self) -> nx.Graph:
        return self.__graph_instance


    @property
    def mandatory_graph(self) -> OrderedSet:
        return self.__mandatory_graph


    @property
    def forbidden_graph(self) -> OrderedSet:
        return self.__forbidden_graph


    @vertices_pedigree_union.setter
    def vertices_pedigree_union(self, vertices_pedigree_union):
        self.__vertices_pedigree_union = vertices_pedigree_union


    @graph_instance.setter
    def graph_instance(self, graph_instance):
        self.__graph_instance = graph_instance


    @mandatory_graph.setter
    def mandatory_graph(self, mandatory_graph):
        self.__mandatory_graph = mandatory_graph


    @forbidden_graph.setter
    def forbidden_graph(self, forbidden_graph):
        self.__forbidden_graph = forbidden_graph


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


    @graph_instance.deleter
    def graph_instance(self):
        del self.__graph_instance


    @mandatory_graph.deleter
    def mandatory_graph(self):
        del self.__mandatory_graph


    @forbidden_graph.deleter
    def forbidden_graph(self):
        del self.__forbidden_graph

    
    def __del__(self):
        del self.__pedigree_family
        del self.__vertices_individuals
        del self.__vertices_mating_units
        del self.__vertices_sibship_units
        del self.__vertices_pedigree_union
        del self.__graph_instance
        del self.__mandatory_graph
        del self.__forbidden_graph


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
        vertices_pedigree_union = OrderedSet()
        vertices_pedigree_union |= OrderedSet(self.vertices_individuals)
        vertices_pedigree_union |= OrderedSet(self.vertices_mating_units)
        vertices_pedigree_union |= OrderedSet(self.vertices_sibship_units)
        return vertices_pedigree_union


    def build_pedigree_graph(self):
        graph_instance = nx.Graph()

        graph_instance.add_nodes_from(self.vertices_individuals)
        graph_instance.add_nodes_from(self.vertices_mating_units)
        graph_instance.add_nodes_from(self.vertices_sibship_units)

        for current_individual in self.vertices_individuals:
            assert isinstance(current_individual, Individual)

            for individual in self.vertices_individuals:
                assert isinstance(individual, Individual)
                if current_individual is not individual:
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
                if current_mating_unit is not mating_unit:
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
                if current_sibship_unit is not sibship_unit:
                    graph_instance.add_edge(current_sibship_unit, sibship_unit)

        return graph_instance


    def build_sets_from_individual(self, individual):
        assert isinstance(individual, Individual)

        pedigree_vertices   =   OrderedSet()
        generation_vertices =   OrderedSet()
        children_vertices   =   OrderedSet()

        pedigree_vertices.add(individual)
        generation_vertices.add(individual.generation_rank)

        for mating_unit in self.vertices_mating_units:
            assert isinstance(mating_unit, MatingUnit)

            condition1 = (individual is mating_unit.male_mate_individual)
            condition2 = (individual is mating_unit.female_mate_individual)

            if condition1 or condition2:
                relation_sibship_unit = mating_unit.sibship_unit_relation

                for sibling in relation_sibship_unit.siblings_individuals:
                    children_vertices.add(sibling)

        return (pedigree_vertices, generation_vertices, children_vertices)


    def build_sets_from_mating_unit(self, mating_unit):
        assert isinstance(mating_unit, MatingUnit)

        pedigree_vertices   =   OrderedSet()
        generation_vertices =   OrderedSet()
        children_vertices   =   OrderedSet()

        pedigree_vertices.add(mating_unit.male_mate_individual)
        pedigree_vertices.add(mating_unit.female_mate_individual)

        generation_vertices.add(mating_unit.male_mate_individual.generation_rank)
        generation_vertices.add(mating_unit.female_mate_individual.generation_rank)

        relation_sibship_unit = mating_unit.sibship_unit_relation

        for sibling in relation_sibship_unit.siblings_individuals:
            children_vertices.add(sibling)

        return (pedigree_vertices, generation_vertices, children_vertices)


    def build_sets_from_sibship_unit(self, sibship_unit):
        assert isinstance(sibship_unit, SibshipUnit)

        pedigree_vertices   =   OrderedSet()
        generation_vertices =   OrderedSet()
        children_vertices   =   OrderedSet()

        for sibling in sibship_unit.siblings_individuals:
            assert isinstance(sibling, Individual)
            pedigree_vertices.add(sibling)
            generation_vertices.add(sibling.generation_rank)

        return (pedigree_vertices, generation_vertices, children_vertices)


    def find_edges_rule_a(self):
        edges_minus = OrderedSet()

        start_index = self.pedigree_family.min_generation_rank
        final_index = self.pedigree_family.max_generation_rank

        for i in range(start_index, final_index + 1):
            current_individuals = self.pedigree_family.get_individuals_by_generation(i)

            for current_individual1 in current_individuals:
                for current_individual2 in current_individuals:
                    if current_individual1 is not current_individual2:
                        edges_minus.add((current_individual1, current_individual2))

        unique_edges = OrderedSet()

        for edge in edges_minus:
            left_vertex = edge[0]
            right_vertex = edge[1]
            reversed_edge = (right_vertex, left_vertex)

            if edge not in unique_edges and reversed_edge not in unique_edges:
                unique_edges.add(edge)

        edges_minus = unique_edges
        return edges_minus


    def find_edges_rule_b(self):
        edges_minus =   OrderedSet()
        edges_plus  =   OrderedSet()

        for individual in self.vertices_individuals:
            for mating_unit in self.vertices_mating_units:
                generation_vertices_1 = self.build_sets_from_individual(individual)[1]
                generation_vertices_2 = self.build_sets_from_mating_unit(mating_unit)[1]

                if generation_vertices_1 == generation_vertices_2:
                    edges_minus.add((individual, mating_unit))

        for individual in self.vertices_individuals:
            for mating_unit in self.vertices_mating_units:
                pedigree_vertices_1 = self.build_sets_from_individual(individual)[0]
                pedigree_vertices_2 = self.build_sets_from_mating_unit(mating_unit)[0]

                if pedigree_vertices_1 <= pedigree_vertices_2:
                    edges_plus.add((individual, mating_unit))

        edges_minus = edges_minus - edges_plus
        return (edges_minus, edges_plus)


    def find_edges_rule_c(self):
        edges_minus =   OrderedSet()
        edges_plus  =   OrderedSet()

        for individual in self.vertices_individuals:
            for sibship_unit in self.vertices_sibship_units:
                generation_vertices_1 = self.build_sets_from_individual(individual)[1]
                generation_vertices_2 = self.build_sets_from_sibship_unit(sibship_unit)[1]
                
                condition1 = individual.individual_father != '0'
                condition2 = individual.individual_mother != '0'

                if  generation_vertices_1 == generation_vertices_2 and \
                    condition1 and condition2:
                    edges_minus.add((individual, sibship_unit))

        for individual in self.vertices_individuals:
            for sibship_unit in self.vertices_sibship_units:
                pedigree_vertices_1 = self.build_sets_from_individual(individual)[0]
                pedigree_vertices_2 = self.build_sets_from_sibship_unit(sibship_unit)[0]

                if pedigree_vertices_1 <= pedigree_vertices_2:
                    edges_plus.add((individual, sibship_unit))

        edges_minus = edges_minus - edges_plus
        return (edges_minus, edges_plus)


    def find_edges_rule_d(self):
        edges_plus  =   OrderedSet()

        for mating_unit in self.vertices_mating_units:
            for sibship_unit in self.vertices_sibship_units:
                children_set = self.build_sets_from_mating_unit(mating_unit)[2]
                pedigree_set = self.build_sets_from_sibship_unit(sibship_unit)[0]

                if children_set == pedigree_set:
                    edges_plus.add((mating_unit, sibship_unit))

        return edges_plus


    def find_edges_rule_e(self):
        edges_minus = OrderedSet()
        units_union = self.vertices_mating_units + self.vertices_sibship_units

        for mating_unit in self.vertices_mating_units:
            for vertex in units_union:
                pedigree_vertices_1 = self.build_sets_from_mating_unit(mating_unit)[0]
                generation_vertices_1 = self.build_sets_from_mating_unit(mating_unit)[1]

                pedigree_vertices_2 = {}
                generation_vertices_2 = {}

                if isinstance(vertex, MatingUnit):
                    pedigree_vertices_2 = self.build_sets_from_mating_unit(vertex)[0]
                    generation_vertices_2 = self.build_sets_from_mating_unit(vertex)[1]
                else:
                    pedigree_vertices_2 = self.build_sets_from_sibship_unit(vertex)[0]
                    generation_vertices_2 = self.build_sets_from_sibship_unit(vertex)[1]

                intersection1 = (pedigree_vertices_1 & pedigree_vertices_2)
                intersection2 = (generation_vertices_1 & generation_vertices_2)

                if len(intersection1) == 0 and len(intersection2) == 0:
                    edges_minus.add((mating_unit, vertex)) 

        edges_minus = edges_minus - self.find_edges_rule_d()
        return edges_minus

    
    def build_mandatory_graph(self):
        return  self.find_edges_rule_b()[1] | \
                self.find_edges_rule_c()[1] | \
                self.find_edges_rule_d()


    def build_forbidden_graph(self):
        return  self.find_edges_rule_a()    | \
                self.find_edges_rule_b()[0] | \
                self.find_edges_rule_c()[0] | \
                self.find_edges_rule_e()


class SandwichInstance:
    def __init__(self, pedigree_vertices, mandatory_graph, forbidden_graph):
        self.__pedigree_vertices    =   pedigree_vertices
        self.__mandatory_graph      =   self.build_graph(mandatory_graph)
        self.__forbidden_graph      =   self.build_graph(forbidden_graph)


    @property
    def pedigree_vertices(self):
        return self.__pedigree_vertices


    @property
    def mandatory_graph(self):
        return self.__mandatory_graph


    @property
    def forbidden_graph(self):
        return self.__forbidden_graph


    @pedigree_vertices.setter
    def pedigree_vertices(self, pedigree_vertices):
        self.__pedigree_vertices = pedigree_vertices


    @mandatory_graph.setter
    def mandatory_graph(self, mandatory_graph):
        self.__mandatory_graph = mandatory_graph


    @forbidden_graph.setter
    def forbidden_graph(self, forbidden_graph):
        self.__forbidden_graph = forbidden_graph


    @pedigree_vertices.deleter
    def pedigree_vertices(self):
        del self.__pedigree_vertices


    @mandatory_graph.deleter
    def mandatory_graph(self):
        del self.__mandatory_graph


    @forbidden_graph.deleter
    def forbidden_graph(self):
        del self.__forbidden_graph

    
    def __del__(self):
        del self.__pedigree_vertices
        del self.__mandatory_graph
        del self.__forbidden_graph


    def build_graph(self, set_edges):
        graph = nx.Graph()
        graph.add_nodes_from(self.pedigree_vertices)
        graph.add_edges_from(set_edges)
        return graph


class SandwichSolver:
    def __init__(self, sandwich_instance):
        assert isinstance(sandwich_instance, SandwichInstance)
        self.__sandwich_instance = sandwich_instance
        self.solved_intervals = self.solve_interval_sandwich_algorithm()


    @property
    def sandwich_instance(self):
        return self.__sandwich_instance


    @sandwich_instance.setter
    def sandwich_instance(self, sandwich_instance):
        self.__sandwich_instance = sandwich_instance


    @sandwich_instance.deleter
    def sandwich_instance(self):
        del self.__sandwich_instance


    def __del__(self):
        del self.__sandwich_instance
        del self.solved_intervals


    def solve_interval_sandwich_algorithm(self):
        cut_realizations = list()
        mandatory_graph_neighbors = dict()

        for vertex in self.sandwich_instance.mandatory_graph.nodes():
            mandatory_graph_neighbors[vertex] = OrderedSet(self.sandwich_instance.mandatory_graph.neighbors(vertex))
        
        for vertex in self.sandwich_instance.pedigree_vertices:
            current_interval = Interval(vertex)
            realization_instance = CutRealization(
                self.sandwich_instance.mandatory_graph,
                self.sandwich_instance.forbidden_graph,
                mandatory_graph_neighbors,
                [current_interval], [vertex]
            )
            cut_realizations.append(realization_instance)

        # Initialize an empty queue Q and 
        # for each v ∈ V, add the cut {v} to Q.
        cut_realizations = deque(cut_realizations)
        layouted_realizations = list()

        # Do the whole loop for the only one feasible cut.
        if len(self.sandwich_instance.pedigree_vertices) == 1:
            current_realization = cut_realizations.pop()
            assert isinstance(current_realization, CutRealization)
            return current_realization.intervals
        
        while len(cut_realizations) != 0:
            # Remove some feasible cut X from Q.
            feasible_cut = cut_realizations.pop()
            assert isinstance(feasible_cut, CutRealization)

            # Store every z ∉ X in an OrderedSet.
            other_vertices = OrderedSet(
                self.sandwich_instance.pedigree_vertices - \
                OrderedSet(feasible_cut.domain_vertex)
            )

            # for every z ∉ X (every element of other_vertices)
            for vertex in other_vertices:
                # Try to extend X by z (using Lemma 2.1).
                condition_extend = feasible_cut.can_extend_vertex(vertex)

                if not condition_extend:
                    continue

                # Suppose a feasible cut Y is generated.
                copy_realization = feasible_cut.create_copy_realization()
                copy_realization.extend_vertex(vertex)
                

                # if Y has domain V then output "success" and stop.
                if  len(copy_realization.domain_vertex) == \
                    len(self.sandwich_instance.pedigree_vertices):
                    return copy_realization.intervals
        
                # Otherwise,...
                else:
                    # ...if Y is new, then add it to Q.
                    if repr(copy_realization) not in layouted_realizations:
                        layouted_realizations.append(repr(copy_realization))
                        cut_realizations.append(copy_realization)

        # Output "failure" and stop.
        return None
