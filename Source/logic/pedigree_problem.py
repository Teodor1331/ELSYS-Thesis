# This Python file uses the following encoding: UTF-8

"""The module has the classes Interval, VertexInterval and Cut.

This module manages the creating of the interval realization
of a Sandwich Graph and implements the needed constraints from
the proposed algorithm for the Interval Graph Sandwich Problem.
"""

from typing import Any
from typing import Union

import copy
import networkx as nx

from ordered_set import OrderedSet

from logic.pedigree_units import Individual
from logic.pedigree_units import MatingUnit
from logic.pedigree_units import SibshipUnit


class Interval:
    """Interval Class.

    This class is used to create the
    abstraction of an interval.
    """

    def __init__(self, left_element=0.0, right_element=1.0) -> None:
        """Initialize an instance of the Interval class.

        It accepts the values of the left and right endpoints.
        """
        try:
            assert isinstance(left_element, float)
            assert isinstance(right_element, float)
        except AssertionError as assertion_error:
            message = 'The interval constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__left_element = left_element
        self.__right_element = right_element

    @property
    def left_element(self) -> float:
        """Return the left element property of the class."""
        return self.__left_element

    @property
    def right_element(self) -> float:
        """Return the right element property of the class."""
        return self.__right_element

    @left_element.setter
    def left_element(self, left_element) -> None:
        assert isinstance(left_element, float)
        self.__left_element = left_element

    @right_element.setter
    def right_element(self, right_element) -> None:
        assert isinstance(right_element, float)
        self.__right_element = right_element

    def intersection(self, interval):
        """Find intersection between two intervals.

        This method finds the intersection between
        two intervals.
        """
        assert isinstance(interval, Interval)

        if self.left_element < interval.right_element:
            return None

        return Interval(
            max(self.left_element, interval.left_element),
            min(self.right_element, interval.right_element)
        )


class VertexInterval(Interval):
    """VertexInterval Class.

    This class is used to create the
    abstraction of an interval for a
    single vertex in a Sandwich Graph.
    """

    def __init__(self, vertex, left_element=0.0, right_element=1.0) -> None:
        """Initialize an instance of the VertexInterval class.

        It accepts the path to the file with the data.
        """
        super().__init__(left_element, right_element)

        try:
            assert isinstance(vertex, (Individual, MatingUnit, SibshipUnit))
        except AssertionError as assertion_error:
            message = 'The vertex interval constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__vertex = vertex

    @property
    def vertex(self) -> Union[Individual, MatingUnit, SibshipUnit]:
        """Return the vertex property of the class."""
        return self.__vertex

    def __repr__(self):
        """Return the string representation of the class."""
        return "Interval(" + str(self.vertex) + ", " + \
               str(self.left_element) + ", " + \
               str(self.right_element) + ")"


class Cut:
    """Cut Class.

    This class is used to manage a cut.
    It can be used to extend a cut and
    to check if it is feasible or not.
    """

    def __init__(self, mandatory_graph, forbidden_graph,
                 graph_neighbors=None, intervals=None,
                 domain_vertex=None, max_width=3,
                 cached_active_vertices=None,
                 cached_maximal_set=None,
                 cached_dangling_set=None,
                 cached_vertex_degree=None) -> None:
        """Initialize an instance of the Cut class.

        It accepts the mandatory graph, the forbidden graph,
        a dict of graph neighbors, intervals, domain vertex
        and max width (the bounded degree of the vertex).
        """
        try:
            assert isinstance(mandatory_graph, nx.Graph)
            assert isinstance(forbidden_graph, nx.Graph)
            assert isinstance(graph_neighbors, (dict, type(None)))
            assert isinstance(intervals, (list, type(None)))
            assert isinstance(domain_vertex, (list, type(None)))
            assert isinstance(max_width, int)
        except AssertionError as assertion_error:
            message = 'The cut constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__mandatory_graph = mandatory_graph
        self.__forbidden_graph = forbidden_graph
        self.__graph_neighbors = graph_neighbors
        self.__intervals = intervals if intervals is not None else []
        self.__domain_vertex = domain_vertex if domain_vertex is not None else []
        self.__max_width = max_width
        self.__domain_set = OrderedSet(self.__domain_vertex)

        self.__graph_neighbors_cache = (
            self.create_graph_neighbors_cache()
            if graph_neighbors is None
            else graph_neighbors
        )

        self.__cached_active_vertices = cached_active_vertices
        self.__cached_maximal_set = cached_maximal_set
        self.__cached_dangling_set = cached_dangling_set
        self.__cached_vertex_degree = (
            cached_vertex_degree
            if cached_vertex_degree is not None
            else {}
        )

    @property
    def mandatory_graph(self) -> nx.Graph:
        """Return the mandatory graph property of the class."""
        return self.__mandatory_graph

    @property
    def forbidden_graph(self) -> nx.Graph:
        """Return the forbidden graph property of the class."""
        return self.__forbidden_graph

    @property
    def graph_neighbors(self) -> Union[dict, None]:
        """Return the graph neighbors property of the class."""
        return self.__graph_neighbors

    @property
    def intervals(self) -> Union[list, None]:
        """Return the intervals property of the class."""
        return self.__intervals

    @property
    def domain_vertex(self) -> Union[list, None]:
        """Return the domain vertex property of the class."""
        return self.__domain_vertex

    @property
    def max_width(self) -> int:
        """Return the max width property of the class."""
        return self.__max_width

    @property
    def domain_set(self) -> OrderedSet:
        """Return the domain set property of the class."""
        return self.__domain_set

    @property
    def graph_neighbors_cache(self) -> dict:
        """Return the graph neighbors cache property of the class."""
        return self.__graph_neighbors_cache

    @property
    def cached_active_vertices(self) -> Union[OrderedSet, None]:
        """Return the cached active vertices property of the class."""
        return self.__cached_active_vertices

    @property
    def cached_maximal_set(self) -> Union[OrderedSet, None]:
        """Return the cached maximal set property of the class."""
        return self.__cached_maximal_set

    @property
    def cached_dangling_set(self) -> Union[OrderedSet, None]:
        """Return the cached dangling set property of the class."""
        return self.__cached_dangling_set

    @property
    def cached_vertex_degree(self) -> dict:
        """Return the cached vertex degree property of the class."""
        return self.__cached_vertex_degree

    def __repr__(self) -> str:
        """Return the string representation of the class."""
        return ";".join(sorted(repr(vertex) for vertex in self.domain_vertex))

    def create_graph_neighbors_cache(self) -> dict:
        """Create graph neighbors cache property."""
        return {
            vertex: OrderedSet(self.mandatory_graph.neighbors(vertex))
            for vertex in self.mandatory_graph.nodes()
        }

    def validate_intervals_ordered(self, vertex1, vertex2) -> bool:
        """Validate if two intervals are ordered."""
        interval1 = self.intervals[vertex1]
        interval2 = self.intervals[vertex2]
        assert isinstance(interval1, Interval)
        assert isinstance(interval2, Interval)
        return interval1.right_element < interval2.left_element

    def validate_maximal_interval(self, index) -> bool:
        """Validate if the interval on the index is the maximal one."""
        for i, _ in enumerate(self.domain_vertex):
            if i != index and self.validate_intervals_ordered(index, i):
                return False

        return True

    def validate_active_vertex(self, vertex) -> bool:
        """Validate if a vertex is from the active region.

        This method checks if a given vertex is from the
        set of the active region vertices in the current
        cut. This is done by making a check if all the
        neighbors of the current vertex are not in the
        domain.
        """
        neighbors = self.graph_neighbors[vertex]

        for neighbor in neighbors:
            if neighbor not in self.domain_set:
                return True

        return False

    def get_active_vertices(self) -> OrderedSet:
        """Get all vertices from the active region.

        This method gets all the vertices from the
        current active region. If it contains already
        these vertices, it returns them. If not, builds
        the set from scratch and returns it as result.
        """
        if self.cached_active_vertices:
            return self.cached_active_vertices

        self.__cached_active_vertices = OrderedSet()

        for vertex in self.domain_vertex:
            if self.validate_active_vertex(vertex):
                self.cached_active_vertices.add(vertex)

        return self.cached_active_vertices

    def get_active_vertex_end_vertices(self, vertex) -> OrderedSet:
        """Get all the endpoints of edges by a vertex.

        This method gets all the endpoint vertices of the
        edges with the given vertex as first one. It returns
        all the vertices that belong to the set of neighbors
        of the given vertex, but do not belong to the domain
        of the current cut.
        """
        return self.graph_neighbors[vertex] - self.domain_set

    def get_interval_by_vertex(self, vertex) -> Interval:
        """Get the interval by a given vertex."""
        index = self.domain_vertex.index(vertex)
        return self.intervals[index]

    def get_degree_vertex(self, vertex) -> Any:
        """Get the degree of a given vertex.

        This method returns the degree of a given vertex.
        The degree of a vertex is the number of edges which
        has the current vertex as an end. First it is checked
        if the degree of the vertex is already computed or not.
        If not, compute it by finding all the intervals which
        has intersection with the interval of the given vertex.
        This is made in order to prevent the possibility of an
        additional edge in the interval graph which is not an
        edge in the required graph in the cut.
        """
        if vertex not in self.cached_vertex_degree:
            vertex_interval = self.get_interval_by_vertex(vertex)
            vertex_interval_edges = []
            assert isinstance(vertex_interval, Interval)

            for interval in self.intervals:
                if vertex_interval.intersection(interval) is not None:
                    vertex_interval_edges.append(interval)

            self.cached_vertex_degree[vertex] = len(vertex_interval_edges) - 1

        return self.cached_vertex_degree[vertex]

    def get_dangling_vertices(self, vertex) -> OrderedSet:
        """Get all the dangling vertices (pendant ones)."""
        return self.get_active_vertex_end_vertices(vertex)

    def get_dangling_set(self) -> OrderedSet:
        """Get the dangling set of the current cut.

        This method returns the dangling set. If the
        dangling set is not computed, it computes it
        by doing a loop through all the active region
        vertices anf for every vertex in the dangling
        vertices, which are result of the current active
        vertex, it adds the presented vertex to the set.
        """
        if self.cached_dangling_set:
            return self.cached_dangling_set

        self.__cached_dangling_set = OrderedSet()

        for active_vertex in self.get_active_vertices():
            for vertex in self.get_dangling_vertices(active_vertex):
                self.cached_dangling_set.add(vertex)

        return self.cached_dangling_set

    def get_maximal_set(self) -> OrderedSet:
        """Get maximal set in the current cut.

        This method returns the maximal set of the current
        cut. If it is empty, it recreates it a cached one.
        For that purpose, it makes a loop through the domain
        vertex and if the validation for the maximal set is
        TRUE for all the vertices, it adds the domain vertex
        in the cached one.
        """
        if self.cached_maximal_set:
            return self.cached_maximal_set

        self.__cached_maximal_set = OrderedSet()

        for i, _ in enumerate(self.domain_vertex):
            if self.validate_maximal_interval(i):
                self.cached_maximal_set.add(self.domain_vertex[i])

        return self.cached_maximal_set

    def build_copy_cut(self) -> Any:
        """Build a copy of the current cut."""
        return Cut(
            self.mandatory_graph, self.forbidden_graph,
            self.graph_neighbors, list(map(copy.copy, self.intervals)),
            copy.copy(self.domain_vertex), self.max_width,
            self.cached_active_vertices,
            self.cached_maximal_set,
            self.cached_dangling_set,
            self.cached_vertex_degree
        )

    def validate_extend_vertex(self, possible_vertex) -> bool:
        """Validate if a cut can be extended with a given vertex.

        This method validates if a cut is feasible with a given
        vertex. It creates a possible cut with a domain vertex of
        the current one domain vertex and the given vertex.
        """
        possible_cut = Cut(
            self.mandatory_graph, self.forbidden_graph,
            self.graph_neighbors, self.intervals + [VertexInterval(possible_vertex)],
            self.domain_vertex + [possible_vertex]
        )

        condition1 = not self.validate_forbidden_edge(possible_vertex)
        condition2 = self.validate_active_region_bounded(possible_vertex, possible_cut)
        condition3 = self.validate_exceeds_max_width(possible_cut)
        condition4 = not self.validate_old_dangling_vertices(possible_vertex, possible_cut)
        condition5 = not self.validate_new_dangling_vertices(possible_vertex, possible_cut)
        condition6 = not self.validate_possible_active_vertex(possible_vertex, possible_cut)

        whole_condition = \
            condition1 or condition2 or condition3 or \
            condition4 or condition5 or condition6

        if whole_condition:
            return False

        assert self.get_active_vertices() <= self.get_maximal_set()
        return True

    def validate_forbidden_edge(self, possible_vertex) -> bool:
        """Validate if there is a forbidden edge in the cut.

        This method validates if there is a forbidden edge between the active
        region vertices of the previous cut and the given vertex. Forbidden edges
        are the set of neighbors of the given vertex from the forbidden graph.
        Active vertices are the active region vertices in the current cut - Δ(X).
        """
        # (v, w) ∉ F (the set of forbidden edges)
        # v         --> possible_vertex
        # w ∈ Δ(X)  --> active_region_vertices
        # F         --> forbidden_vertices

        forbidden_vertices = OrderedSet(self.forbidden_graph.neighbors(possible_vertex))
        active_region_vertices = self.get_active_vertices()
        return len(forbidden_vertices & active_region_vertices) == 0

    def validate_active_region_bounded(self, possible_vertex, cut) -> bool:
        """Validate if the active region has been bounded.

        This method validates if the active region has been bounded. There
        are two conditions which makes the active region bounded.

        The first one is if the length of the active region vertices is
        already the bounded width - 1. The method makes an inner validation
        in case the given vertex is not in the dangling set of the current cut.

        The second one is made with taking the section of the old vertices in
        the active region and the new vertices in the active region. For every
        single one of them, the method validates if the degree on the current
        active vertex in the current cut has a degree with a value as same as
        the value of the degree of the same active vertex in the old cut + 1.
        """
        assert isinstance(cut, Cut)

        if len(self.get_active_vertices()) == self.max_width - 1:
            if possible_vertex not in self.get_dangling_set():
                return True

        active_vertices = self.get_active_vertices() & cut.get_active_vertices()
        for active in active_vertices:
            if cut.get_degree_vertex(active) != self.get_degree_vertex(active) + 1:
                return True

        return False

    def validate_exceeds_max_width(self, cut) -> bool:
        """Validate if the max width is exceeded.

        This method validates if the active region has already on its
        bounds or bigger in order to decide if we can exceed the cut.
        """
        assert isinstance(cut, Cut)
        return len(cut.get_active_vertices()) >= cut.max_width

    def validate_old_dangling_vertices(self, possible_vertex, cut) -> bool:
        """Validate all the old dangling edges.

        This method validates all the old dangling edges. First,
        for every vertex in the active region, the method takes
        its dangling ones. Then it takes the dangling ones of the
        given vertex, but in the upcoming cut. The method changes
        the dangling vertex region so that it can contain only
        the vertices which have been in the set before the set
        before the assignment, but not taking the given vertex
        in mind.
        """
        assert isinstance(cut, Cut)

        for active_vertex in self.get_active_vertices():
            dangling_vertex_region = self.get_dangling_vertices(active_vertex)
            new_dangling_vertex_region = cut.get_dangling_vertices(active_vertex)
            dangling_vertex_region -= OrderedSet([possible_vertex])

            if dangling_vertex_region != new_dangling_vertex_region:
                return False

        return True

    def validate_new_dangling_vertices(self, possible_vertex, cut) -> bool:
        """Validate all the new dangling edges.

        This method validates all the new dangling edges. First,
        the method takes all the endpoints of the edges with a
        start one the given vertex. In new_edges, the method gets
        the difference from the neighbors in the required graph
        and the active region vertices and, at the end, validates
        for the equality between new_dangling and new_edges.
        """
        assert isinstance(cut, Cut)
        new_dangling = cut.get_dangling_vertices(possible_vertex)
        new_edges = (
            OrderedSet(self.mandatory_graph.neighbors(possible_vertex)) -
            self.get_active_vertices()
        )
        return new_dangling == new_edges

    def validate_possible_active_vertex(self, possible_vertex, cut) -> bool:
        """Validate if the given vertex can be a valid active one.

        This method validates if the given vertex can be a valid active one.
        First, the method takes the active region vertices of the cut it
        has been given. Then it gets the union of the vertices in the active
        region in the current cut and the possible vertex. For every vertex
        in the union, it is made a validation if there are dangling vertices.
        If there are, the method adds the vertex to a new set.
        """
        assert isinstance(cut, Cut)
        possible_active_region = cut.get_active_vertices()
        union_active_region = self.get_active_vertices() | OrderedSet([possible_vertex])
        expected_active_region = OrderedSet()

        for vertex in union_active_region:
            if len(cut.get_dangling_vertices(vertex)) != 0:
                expected_active_region.add(vertex)

        return possible_active_region == expected_active_region

    def extend_vertex(self, possible_vertex) -> bool:
        """Extend the vertex with a possible vertex."""
        if not self.validate_extend_vertex(possible_vertex):
            return False

        # Every time a cut is extended with a given vertex, one
        # should find the maximal right end from all the right ends
        # in the intervals. In order to make an extension, one
        # need to make a shift by the average value of the range
        # defined the intervals, in our case, this is 0.5.
        # It is made shift by this value and the maximal right value.

        max_right_value = next(
            self.get_interval_by_vertex(v).right_element
            for v in self.get_maximal_set()
        )
        interval_shift = max_right_value + 0.5

        # For all the active vertices in the current cut the
        # right end of the interval is shifted from the already
        # shifted value variable.

        for active_vertex in self.get_active_vertices():
            interval = self.get_interval_by_vertex(active_vertex)
            assert isinstance(interval, Interval)
            interval.right_element = interval_shift + 1

        # When the active vertices are extended, it is added the possible
        # vertex corresponding interval in the interval set in the
        # current cut. The difference of 1 between left end of the interval
        # and the right end of the interval is prevented.

        self.domain_vertex.append(possible_vertex)
        self.intervals.append(VertexInterval(possible_vertex, interval_shift, interval_shift + 1))
        self.domain_set.add(possible_vertex)

        # After extension of the current vertex has been
        # done, everything is returned to empty / None for
        # possible next computations and operations.

        self.__cached_active_vertices = None
        self.__cached_maximal_set = None
        self.__cached_dangling_set = None
        self.__cached_vertex_degree = {}
        return True
