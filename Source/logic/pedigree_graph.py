# This Python file uses the following encoding: UTF-8

"""This module has the classes Graph, SandwichInstance and ProblemSolver.

This module contains the whole logic for creating the edges in the
graph, which will be used later to solve the Interval Graph Sandwich
Problem with the Interval Graph Sandwich Algorithm.
"""

from collections import deque
from typing import AbstractSet
from typing import Union
from ordered_set import OrderedSet

import networkx as nx

from logic.pedigree_units import Individual
from logic.pedigree_units import MatingUnit
from logic.pedigree_units import SibshipUnit
from logic.pedigree_family import PedigreeFamily
from logic.pedigree_problem import VertexInterval
from logic.pedigree_problem import Cut


class Graph:
    """Graph Class.

    This class is used to create the graph
    with the mandatory subgraph and the
    forbidden subgraph from a pedigree.
    """

    def __init__(self, pedigree_family: PedigreeFamily):
        """Initialize an instance of the Graph class.

        It accepts an instance of the PedigreeFamily class.
        """
        try:
            assert isinstance(pedigree_family, PedigreeFamily)
        except AssertionError as assertion_error:
            message = 'The graph constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__pedigree_family = pedigree_family
        self.__vertices_individuals = self.build_vertices_individuals()
        self.__vertices_mating_units = self.build_vertices_mating_units()
        self.__vertices_sibship_units = self.build_vertices_sibship_units()
        self.__vertices_pedigree_union = self.build_vertices_pedigree_union()

        self.__mandatory_graph = self.build_mandatory_graph()
        self.__forbidden_graph = self.build_forbidden_graph()

    @property
    def pedigree_family(self) -> PedigreeFamily:
        """Return the pedigree graph property of the class."""
        return self.__pedigree_family

    @property
    def vertices_individuals(self) -> list:
        """Return the vertices individuals property of the class."""
        return self.__vertices_individuals

    @property
    def vertices_mating_units(self) -> list:
        """Return the vertices mating units property of the class."""
        return self.__vertices_mating_units

    @property
    def vertices_sibship_units(self) -> list:
        """Return the vertices sibship units property of the class."""
        return self.__vertices_sibship_units

    @property
    def vertices_pedigree_union(self) -> AbstractSet:
        """Return the vertices pedigree union property of the class."""
        return self.__vertices_pedigree_union

    @property
    def mandatory_graph(self) -> AbstractSet:
        """Return the mandatory graph property of the class."""
        return self.__mandatory_graph

    @property
    def forbidden_graph(self) -> AbstractSet:
        """Return the forbidden graph property of the class."""
        return self.__forbidden_graph

    def build_vertices_individuals(self) -> list:
        """Build the vertices of the individuals."""
        vertices_individuals = []

        for key in self.pedigree_family.pedigree_individuals:
            individual = self.pedigree_family.pedigree_individuals[key]
            assert isinstance(individual, Individual)
            vertices_individuals.append(individual)

        return vertices_individuals

    def build_vertices_mating_units(self) -> list:
        """Build the vertices of the mating units."""
        vertices_mating_units = []

        for key in self.pedigree_family.pedigree_mating_units:
            mating_unit = self.pedigree_family.pedigree_mating_units[key]
            assert isinstance(mating_unit, MatingUnit)
            vertices_mating_units.append(mating_unit)

        return vertices_mating_units

    def build_vertices_sibship_units(self) -> list:
        """Build the vertices of the sibship units."""
        vertices_sibship_units = []

        for key in self.pedigree_family.pedigree_sibship_units:
            sibship_unit = self.pedigree_family.pedigree_sibship_units[key]
            assert isinstance(sibship_unit, SibshipUnit)
            vertices_sibship_units.append(sibship_unit)

        return vertices_sibship_units

    def build_vertices_pedigree_union(self) -> AbstractSet:
        """Build the union of all the vertices."""
        vertices_pedigree_union = OrderedSet()
        vertices_pedigree_union |= OrderedSet(self.vertices_individuals)
        vertices_pedigree_union |= OrderedSet(self.vertices_mating_units)
        vertices_pedigree_union |= OrderedSet(self.vertices_sibship_units)
        return vertices_pedigree_union

    def build_sets_from_individual(self, individual: Individual) -> tuple:
        """Build the needed sets from an individual.

        This method builds the sets p(v), g(v) and c(v)
        of a single vertex v, where v is an individual.
        """
        assert isinstance(individual, Individual)

        pedigree_vertices = OrderedSet()
        generation_vertices = OrderedSet()
        children_vertices = OrderedSet()

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

        return pedigree_vertices, generation_vertices, children_vertices

    def build_sets_from_mating_unit(self, mating_unit: MatingUnit) -> tuple:
        """Build the needed sets from a mating unit.

        This method builds the sets p(v), g(v) and c(v)
        of a single vertex v, where v is a mating unit.
        """
        assert isinstance(mating_unit, MatingUnit)

        pedigree_vertices = OrderedSet()
        generation_vertices = OrderedSet()
        children_vertices = OrderedSet()

        pedigree_vertices.add(mating_unit.male_mate_individual)
        pedigree_vertices.add(mating_unit.female_mate_individual)

        generation_vertices.add(mating_unit.male_mate_individual.generation_rank)
        generation_vertices.add(mating_unit.female_mate_individual.generation_rank)

        relation_sibship_unit = mating_unit.sibship_unit_relation

        for sibling in relation_sibship_unit.siblings_individuals:
            children_vertices.add(sibling)

        return pedigree_vertices, generation_vertices, children_vertices

    def build_sets_from_sibship_unit(self, sibship_unit: SibshipUnit) -> tuple:
        """Build the needed sets from a sibship unit.

        This method builds the sets p(v), g(v) and c(v)
        of a single vertex v, where v is a sibship unit.
        """
        assert isinstance(sibship_unit, SibshipUnit)

        pedigree_vertices = OrderedSet()
        generation_vertices = OrderedSet()
        children_vertices = OrderedSet()

        for sibling in sibship_unit.siblings_individuals:
            assert isinstance(sibling, Individual)
            pedigree_vertices.add(sibling)
            generation_vertices.add(sibling.generation_rank)

        return pedigree_vertices, generation_vertices, children_vertices

    def find_edges_rule_a(self) -> OrderedSet:
        """Find all the edges for rule A.

        This method returns exactly 1 set of edges.
        """
        edges_minus = OrderedSet()

        start_index = self.pedigree_family.min_generation_rank
        final_index = self.pedigree_family.max_generation_rank

        for i in range(start_index, final_index + 1):
            current_individuals = self.pedigree_family.get_individuals_by_generation(i)

            for current_individual1 in current_individuals:
                for current_individual2 in current_individuals:
                    assert isinstance(current_individual1, Individual)
                    assert isinstance(current_individual2, Individual)

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

    def find_edges_rule_b(self) -> tuple:
        """Find all the edges for rule B.

        This method returns exactly 2 sets of edges.
        """
        edges_minus = OrderedSet()
        edges_plus = OrderedSet()

        for individual in self.vertices_individuals:
            for mating_unit in self.vertices_mating_units:
                assert isinstance(individual, Individual)
                assert isinstance(mating_unit, MatingUnit)

                generation_vertices_1 = self.build_sets_from_individual(individual)[1]
                generation_vertices_2 = self.build_sets_from_mating_unit(mating_unit)[1]

                if generation_vertices_1 == generation_vertices_2:
                    edges_minus.add((individual, mating_unit))

        for individual in self.vertices_individuals:
            for mating_unit in self.vertices_mating_units:
                assert isinstance(individual, Individual)
                assert isinstance(mating_unit, MatingUnit)

                pedigree_vertices_1 = self.build_sets_from_individual(individual)[0]
                pedigree_vertices_2 = self.build_sets_from_mating_unit(mating_unit)[0]

                if pedigree_vertices_1 <= pedigree_vertices_2:
                    edges_plus.add((individual, mating_unit))

        edges_minus -= edges_plus
        return edges_minus, edges_plus

    def find_edges_rule_c(self) -> tuple:
        """Find all the edges for rule C.

        This method returns exactly 2 sets of edges.
        """
        edges_minus = OrderedSet()
        edges_plus = OrderedSet()

        for individual in self.vertices_individuals:
            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(individual, Individual)
                assert isinstance(sibship_unit, SibshipUnit)

                generation_vertices_1 = self.build_sets_from_individual(individual)[1]
                generation_vertices_2 = self.build_sets_from_sibship_unit(sibship_unit)[1]

                condition1 = individual.individual_father != '0'
                condition2 = individual.individual_mother != '0'

                if generation_vertices_1 == generation_vertices_2 and \
                   condition1 and condition2:
                    edges_minus.add((individual, sibship_unit))

        for individual in self.vertices_individuals:
            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(individual, Individual)
                assert isinstance(sibship_unit, SibshipUnit)

                pedigree_vertices_1 = self.build_sets_from_individual(individual)[0]
                pedigree_vertices_2 = self.build_sets_from_sibship_unit(sibship_unit)[0]

                if pedigree_vertices_1 <= pedigree_vertices_2:
                    edges_plus.add((individual, sibship_unit))

        edges_minus -= edges_plus
        return edges_minus, edges_plus

    def find_edges_rule_d(self) -> OrderedSet:
        """Find all the edges for rule D.

        This method returns exactly 1 set of edges.
        """
        edges_plus = OrderedSet()

        for mating_unit in self.vertices_mating_units:
            for sibship_unit in self.vertices_sibship_units:
                assert isinstance(mating_unit, MatingUnit)
                assert isinstance(sibship_unit, SibshipUnit)

                children_set = self.build_sets_from_mating_unit(mating_unit)[2]
                pedigree_set = self.build_sets_from_sibship_unit(sibship_unit)[0]

                if children_set == pedigree_set:
                    edges_plus.add((mating_unit, sibship_unit))

        return edges_plus

    def find_edges_rule_e(self) -> OrderedSet:
        """Find all the edges for rule E.

        This method returns exactly 1 set of edges.
        """
        edges_minus = OrderedSet()
        units_union = self.vertices_mating_units + self.vertices_sibship_units

        for mating_unit in self.vertices_mating_units:
            assert isinstance(mating_unit, MatingUnit)

            for vertex in units_union:
                pedigree_vertices_1 = self.build_sets_from_mating_unit(mating_unit)[0]
                generation_vertices_1 = self.build_sets_from_mating_unit(mating_unit)[1]

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

        edges_minus -= self.find_edges_rule_d()
        return edges_minus

    def build_mandatory_graph(self) -> OrderedSet:
        """Build the mandatory graph.

        This method returns the edges union,
        which is needed for the mandatory graph.
        """
        return self.find_edges_rule_b()[1] | \
            self.find_edges_rule_c()[1] | \
            self.find_edges_rule_d()

    def build_forbidden_graph(self) -> OrderedSet:
        """Build the forbidden graph.

        This method returns the edges union,
        which is needed for the forbidden graph.
        """
        return self.find_edges_rule_a() | \
            self.find_edges_rule_b()[0] | \
            self.find_edges_rule_c()[0] | \
            self.find_edges_rule_e()


class SandwichInstance:
    """SandwichInstance Class.

    This class is used to manage a sandwich instance.
    """

    def __init__(self,
                 pedigree_vertices: AbstractSet,
                 mandatory_graph: AbstractSet,
                 forbidden_graph: AbstractSet) -> None:
        """Initialize an instance of the SandwichInstance class.

        It accepts a set of vertices, a set of mandatory
        edges and a set of forbidden edges.
        """
        try:
            assert isinstance(pedigree_vertices, AbstractSet)
            assert isinstance(mandatory_graph, AbstractSet)
            assert isinstance(forbidden_graph, AbstractSet)
        except AssertionError as assertion_error:
            message = 'The sandwich instance constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__pedigree_vertices = pedigree_vertices
        self.__mandatory_graph = self.build_graph(mandatory_graph)
        self.__forbidden_graph = self.build_graph(forbidden_graph)

    @property
    def pedigree_vertices(self) -> OrderedSet:
        """Return the pedigree vertices of the class."""
        return self.__pedigree_vertices

    @property
    def mandatory_graph(self) -> nx.Graph:
        """Return the mandatory graph property of the class."""
        return self.__mandatory_graph

    @property
    def forbidden_graph(self) -> nx.Graph:
        """Return the forbidden graph property of the class."""
        return self.__forbidden_graph

    def build_graph(self, set_edges) -> nx.Graph:
        """Build a graph by its edges and the pedigree vertices."""
        graph = nx.Graph()
        graph.add_nodes_from(self.pedigree_vertices)
        graph.add_edges_from(set_edges)
        return graph


class ProblemSolver:
    """ProblemSolver Class.

    This class is used to solve the
    Interval Graph Sandwich Problem
    and to find its interval realization.
    """

    def __init__(self, sandwich_instance: SandwichInstance) -> None:
        """Initialize an instance of the ProblemSolver class.

        It accepts an instance of the SandwichInstance class.
        """
        try:
            assert isinstance(sandwich_instance, SandwichInstance)
        except AssertionError as assertion_error:
            message = 'The sandwich solver constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error
        self.__sandwich_instance = sandwich_instance
        self.__solved_intervals = self.solve_interval_graph_sandwich_problem()

    @property
    def sandwich_instance(self) -> SandwichInstance:
        """Return the sandwich instance property of the class."""
        return self.__sandwich_instance

    @property
    def solved_intervals(self) -> list:
        """Return the solved intervals property of the class."""
        return self.__solved_intervals

    def solve_interval_graph_sandwich_problem(self) -> Union[list, None]:
        """Solve the Interval Graph Sandwich Problem.

        This method is used to solve the IGS Problem
        with the prooved algorithm from the article:
        "Bounded Degree Interval Sandwich Problem"
        """
        cut_realizations = []
        mandatory_graph_neighbors = {}

        for vertex in self.sandwich_instance.mandatory_graph.nodes():
            mandatory_graph_neighbors[vertex] = OrderedSet(
                self.sandwich_instance.mandatory_graph.neighbors(vertex)
            )

        # For each v ∈ V, add the cut {v} to Q.
        for vertex in self.sandwich_instance.pedigree_vertices:
            current_interval = VertexInterval(vertex)
            realization_instance = Cut(
                self.sandwich_instance.mandatory_graph,
                self.sandwich_instance.forbidden_graph,
                mandatory_graph_neighbors,
                [current_interval], [vertex]
            )
            cut_realizations.append(realization_instance)

        # Initialize an empty queue Q.
        cut_realizations = deque(cut_realizations)
        layouted_realizations = []

        # Do the whole loop for the only one feasible cut.
        if len(self.sandwich_instance.pedigree_vertices) == 1:
            current_realization = cut_realizations.pop()
            assert isinstance(current_realization, Cut)
            return current_realization.intervals

        while len(cut_realizations) != 0:
            # Remove some feasible cut X from Q.
            feasible_cut = cut_realizations.pop()
            assert isinstance(feasible_cut, Cut)

            # Store every z ∉ X in an OrderedSet.
            other_vertices = OrderedSet(
                self.sandwich_instance.pedigree_vertices -
                OrderedSet(feasible_cut.domain_vertex)
            )

            # For every z ∉ X (every element of other_vertices), do:
            for vertex in other_vertices:
                # Try to extend X by z (using Lemma 2.1).
                condition_extend = feasible_cut.validate_extend_vertex(vertex)

                if not condition_extend:
                    continue

                # Suppose a feasible cut Y is generated.
                copy_realization = feasible_cut.build_copy_cut()
                copy_realization.extend_vertex(vertex)

                # If Y has domain V then output "success" and stop.
                if len(copy_realization.domain_vertex) == \
                   len(self.sandwich_instance.pedigree_vertices):
                    return copy_realization.intervals

                # Otherwise, if Y is new, then add it to Q.
                if repr(copy_realization) not in layouted_realizations:
                    layouted_realizations.append(repr(copy_realization))
                    cut_realizations.append(copy_realization)

        # Output "failure" and stop.
        return None
