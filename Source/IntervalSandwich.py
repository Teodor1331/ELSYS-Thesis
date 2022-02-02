import networkx as nx
import copy

from ordered_set import OrderedSet


class Interval:
    def __init__(self, vertex, left_element = 0.0, right_element = 1.0):
        self.__vertex           =   vertex
        self.__left_element     =   left_element
        self.__right_element    =   right_element


    @property
    def vertex(self):
        return self.__vertex

    
    @property
    def left_element(self):
        return self.__left_element


    @property
    def right_element(self):
        return self.__right_element


    @vertex.setter
    def vertex(self, vertex):
        self.__vertex = vertex


    @left_element.setter
    def left_element(self, left_element):
        self.__left_element = left_element


    @right_element.setter
    def right_element(self, right_element):
        self.__right_element = right_element


    def __repr__(self):
        return  "Interval(" + str(self.vertex) + ", " + \
                str(self.left_element) + ", " + \
                str(self.right_element) + ")"


    def __del__(self):
        del self.__vertex
        del self.__left_element
        del self.__right_element


    def find_intersection(self, interval):
        assert isinstance(interval, Interval)

        if self.left_element < interval.right_element:
            return None

        return Interval(
            max(self.left_element, interval.left_element),
            min(self.right_element, interval.right_element)
        )


class CutRealization:
    def __init__(self, required_graph, forbidden_graph, graph_neighbors = None, intervals = None, domain_vertex = None, max_width = 3,
    cached_active_vertices = None, cached_maximal_set = None, cached_dangling_set = None, cached_vertex_degree = None):
        assert isinstance(required_graph, nx.Graph)
        assert isinstance(forbidden_graph, nx.Graph)
        assert isinstance(graph_neighbors, (dict, None))
        assert isinstance(intervals, (list, None))
        assert isinstance(domain_vertex, (list, None))
        assert isinstance(max_width, int)

        self.__required_graph       =   required_graph
        self.__forbidden_graph      =   forbidden_graph
        self.__graph_neighbors      =   graph_neighbors
        self.__intervals            =   intervals if intervals != None else []
        self.__domain_vertex        =   domain_vertex if domain_vertex != None else []
        self.__max_width            =   max_width
        self.__domain_set           =   OrderedSet(self.__domain_vertex)

        self.__graph_neighbors_cache = self.create_graph_neighbors_cache() if graph_neighbors is None else graph_neighbors
        self.__cached_active_vertices = cached_active_vertices
        self.__cached_maximal_set = cached_maximal_set
        self.__cached_dangling_set = cached_dangling_set
        self.__cached_vertex_degree = cached_vertex_degree if cached_vertex_degree is not None else {}


    @property
    def required_graph(self):
        return self.__required_graph


    @property
    def forbidden_graph(self):
        return self.__forbidden_graph


    @property
    def graph_neighbors(self):
        return self.__graph_neighbors


    @property
    def intervals(self):
        return self.__intervals


    @property
    def domain_vertex(self):
        return self.__domain_vertex

    @property
    def max_width(self):
        return self.__max_width


    @property
    def domain_set(self):
        return self.__domain_set


    @property
    def graph_neighbors_cache(self):
        return self.__graph_neighbors_cache


    @required_graph.setter
    def required_graph(self, required_graph):
        self.__required_graph = required_graph


    @forbidden_graph.setter
    def forbidden_graph(self, forbidden_graph):
        self.__forbidden_graph = forbidden_graph


    @graph_neighbors.setter
    def graph_neighbors(self, graph_neighbors):
        self.__graph_neighbors = graph_neighbors


    @intervals.setter
    def intervals(self, intervals):
        self.__intervals = intervals


    @domain_vertex.setter
    def domain_vertex(self, domain_vertex):
        self.__domain_vertex = domain_vertex

    
    @graph_neighbors_cache.setter
    def graph_neighbors_cache(self, graph_neighbors_cache):
        self.__graph_neighbors_cache = graph_neighbors_cache


    @required_graph.deleter
    def required_graph(self):
        del self.__required_graph


    @forbidden_graph.deleter
    def forbidden_graph(self):
        del self.__forbidden_graph


    @graph_neighbors.deleter
    def graph_neighbors(self):
        del self.__graph_neighbors


    @intervals.deleter
    def intervals(self):
        del self.__intervals


    @domain_vertex.deleter
    def domain_vertex(self):
        del self.__domain_vertex


    @graph_neighbors_cache.deleter
    def graph_neighbors_cache(self):
        del self.__graph_neighbors_cache


    def __del__(self):
        del self.__required_graph
        del self.__forbidden_graph
        del self.__graph_neighbors
        del self.__intervals
        del self.__domain_vertex
        del self.__max_width
        del self.__domain_set

        del self.__graph_neighbors_cache
        del self.__cached_active_vertices
        del self.__cached_dangling_set
        del self.__cached_maximal_set
        del self.__cached_vertex_degree


    def __repr__(self):
        return ";".join(sorted(repr(vertex) for vertex in self.domain_vertex))


    def check_active_vertex(self, vertex):
        # Check if a vertex is from the set
        # of the active region vertices in the
        # current feasible cut. The function
        # checks if all the neighbors of the
        # current vertex are not in the domain.

        neighbors = self.graph_neighbors[vertex]

        for neighbor in neighbors:
            if neighbor not in self.domain_set:
                return True

        return False


    def get_active_vertices(self):
        # Get all of the vertices from the
        # current active region. If it contains
        # already these vertices, return them.
        # If not, build the set from scratch
        # and, at last, return it as result.

        if self.__cached_active_vertices:
            return self.__cached_active_vertices

        self.__cached_active_vertices = OrderedSet()

        for vertex in self.domain_vertex:
            if self.check_active_vertex(vertex):
                self.__cached_active_vertices.add(vertex)

        return self.__cached_active_vertices


    def get_active_vertex_end_vertices(self, vertex):
        # Get all the ends of the edges with the current
        # vertex as first vertex. We return all the vertices
        # that belong to the set of neighbors of the current
        # vertex, but do not belong to the domain set of the
        # current realization.
        return self.graph_neighbors[vertex] - self.domain_set


    def get_interval_by_vertex(self, vertex):
        # Get the corresponding interval by
        # given vertex. This is a fast utility
        # function for readability of the code.

        index = self.domain_vertex.index(vertex)
        return self.intervals[index]

    def degree_vertex(self, vertex):
        # The function returns the degree of a vertex.
        # The degree of a vertex is the number of edges
        # which has the current vertex as an end.

        # First we check if the degree of the vertex is
        # already computed and return it if it is.
        # If not, we caclulate it by finding all the intervals
        # which has intersection with the interval of the
        # current vertex. Here we make this in order to prevent
        # the possibility of an additional edge in the interval graph
        # which is not an edge in the required graph in the realization.

        if vertex not in self.__cached_vertex_degree:
            vertex_interval = self.get_interval_by_vertex(vertex)
            vertex_interval_edges = list()
            assert isinstance(vertex_interval, Interval)

            for interval in self.intervals:
                if vertex_interval.find_intersection(interval) is not None:
                    vertex_interval_edges.append(interval)

            self.__cached_vertex_degree[vertex] = len(vertex_interval_edges) - 1

        return self.__cached_vertex_degree[vertex]


    def dangling_vertices(self, vertex):
        # The function get all the dangling vertices (pendant ones).
        return self.get_active_vertex_end_vertices(vertex)


    def dangling_set(self):
        # The function returns the dangling set.
        # If the dangling set is already computed,
        # directly return it. If it is not, we
        # compute it by doing a loop through all
        # the active region vertices and for every
        # vertex in the dangling vertices, which are
        # result of the current active vertx, we add
        # the presented vertex to the set.

        if self.__cached_dangling_set:
            return self.__cached_dangling_set

        self.__cached_dangling_set = OrderedSet()

        for active_vertex in self.get_active_vertices():
            for vertex in self.dangling_vertices(active_vertex):
                self.__cached_dangling_set.add(vertex)

        return self.__cached_dangling_set


    def are_intervals_ordered(self, vertex1, vertex2):
        # Utility function to check if two intervals
        # are in the right order. We check this by
        # comparing the right end of the first interval
        # with the left end of the second interval.

        interval1 = self.intervals[vertex1]
        interval2 = self.intervals[vertex2]
        assert isinstance(interval1, Interval)
        assert isinstance(interval2, Interval)
        return interval1.right_element < interval2.left_element


    def check_maximal_interval(self, index):
        # By a given index, the function checks for
        # every vertex in the domain vertices if the
        # current index is not the given index and
        # if the intervals are ordered as expected.

        for i, _ in enumerate(self.domain_vertex):
            if i != index and self.are_intervals_ordered(index, i):
                return False

        return True


    def get_maximal_set(self):
        # The function returns the maximal set of
        # the current realization. If it is empty
        # the function recreates it as cached one.
        # For that purpose, it makes a loop through
        # the domain vertex and if the validation of
        # the maximal set is TRUE for all the vertices,
        # we add the domain vertex in the cached one.

        if self.__cached_maximal_set:
            return self.__cached_maximal_set

        self.__cached_maximal_set = OrderedSet()

        for i in range(len(self.domain_vertex)):
            if self.check_maximal_interval(i):
                self.__cached_maximal_set.add(self.domain_vertex[i])

        return self.__cached_maximal_set


    def create_graph_neighbors_cache(self):
        return {
            vertex: OrderedSet(self.required_graph.neighbors(vertex))
            for vertex in self.required_graph.nodes()
        }

    def create_copy_realization(self):
        return CutRealization(
            self.required_graph, self.forbidden_graph,
            self.graph_neighbors, list(map(copy.copy, self.intervals)),
            copy.copy(self.domain_vertex), self.max_width,
            self.__cached_active_vertices,
            self.__cached_maximal_set,
            self.__cached_dangling_set,
            self.__cached_vertex_degree
        )

    def can_extend_vertex(self, possible_vertex):
        temporary_realization = CutRealization(
            self.required_graph, self.forbidden_graph,
            self.graph_neighbors, self.intervals + [Interval(possible_vertex)],
            self.domain_vertex + [possible_vertex]
        )

        condition1 = not self.check_forbidden_edge(possible_vertex)
        condition2 = self.check_active_region_bounded(possible_vertex, temporary_realization)
        condition3 = self.exceeds_max_width(temporary_realization)
        condition4 = not self.validate_old_dangling_vertices(possible_vertex, temporary_realization)
        condition5 = not self.validate_new_dangling_vertices(possible_vertex, temporary_realization)
        condition6 = not self.validate_possible_active_vertex(possible_vertex, temporary_realization)

        whole_condition = \
            condition1 or condition2 or condition3 or \
            condition4 or condition5 or condition6

        if whole_condition:
            return False

        assert self.get_active_vertices() <= self.get_maximal_set()
        return True

    # A function to check if there is a forbidden edge between the
    # active region vertices of the previous realization and the current 
    # vertex. Forbidden vertices are the set of neighbors of the current
    # vertex from the forbidden graph. Active vertices are the active 
    # region vertice in the current realization - Δ(X).

    def check_forbidden_edge(self, possible_vertex):
        # (v, w) ∉ F (the set of forbidden edges)
        # v         --> possible_vertex
        # w ∈ Δ(X)  --> active_region_vertices
        # F         --> forbidden_vertices

        forbidden_vertices = OrderedSet(self.forbidden_graph.neighbors(possible_vertex))
        active_region_vertices = self.get_active_vertices()
        return len(forbidden_vertices & active_region_vertices) == 0


    def check_active_region_bounded(self, possible_vertex, realization):
        # The function checks if the active region has been bounded.
        # There are two conditions which makes the active region
        # bounded. 
        # 
        # The first one is if length of the active region
        # vertices is already the bounded width - 1. We make an inner
        # check in case the possible vertex is not in the dangling set
        # of the current realization.
        #
        # For the second one we take the section of the old vertices
        # in the active region and the new vertices in the active region.
        # For every single one of them, we check if the degree of the
        # current active vertex in the current realization is has a degree of
        # the degree of the same active vertex in the old realization + 1.
        # If for all of the active vertices, this condition is True, we have
        # passed the validation correctly.

        assert isinstance(realization, CutRealization)

        if len(self.get_active_vertices()) == self.max_width - 1:
            if possible_vertex not in self.dangling_set():
                return True

        active_vertices = self.get_active_vertices() & realization.get_active_vertices()
        for active in active_vertices:
            if realization.degree_vertex(active) != self.degree_vertex(active) + 1:
                return True

        return False


    def exceeds_max_width(self, realization):
        # The function checks if the active region has already on its
        # bounds or bigger. If it is already our max_width, we know
        # that we can't extend with more vertices from here.

        assert isinstance(realization, CutRealization)
        return len(realization.get_active_vertices()) >= realization.max_width


    def validate_old_dangling_vertices(self, possible_vertex, realization):
        # This function validates all the old dangling edges.
        # First, for every vertex in the active region, we
        # take its danling ones. Then we take the dangling
        # ones of this vertex, but in the upcoming realization.
        # We change the dangling vertex region so that it can
        # contains only the vertices which have been in the
        # set before the assignment, but not taking the possible
        # vertex in mind. If the two sets after all are same for
        # every active vertex, we have passed the validation.

        assert isinstance(realization, CutRealization)

        for active_vertex in self.get_active_vertices():
            dangling_vertex_region = self.dangling_vertices(active_vertex)
            new_dangling_vertex_region = realization.dangling_vertices(active_vertex)
            dangling_vertex_region = dangling_vertex_region - OrderedSet([possible_vertex])

            if dangling_vertex_region != new_dangling_vertex_region:
                return False

        return True

    def validate_new_dangling_vertices(self, possible_vertex, realization):
        # This function validates all the new dangling edges.
        # First, we get all the end vertices with a start one
        # possible vertex. In new edges we get the difference
        # from the neighbors in the required graph and the
        # active region vertices. If the two sets are same, we
        # have passed the validation correctly.
        
        assert isinstance(realization, CutRealization)
        new_dangling = realization.dangling_vertices(possible_vertex)
        new_edges = OrderedSet(self.required_graph.neighbors(possible_vertex)) - self.get_active_vertices()
        return new_dangling == new_edges


    def validate_possible_active_vertex(self, possible_vertex, realization):
        # The function checks if the possible vertex can be a valid
        # active vertex. First we get the active region vertices of the
        # realization we have created. Then we get the union of the
        # vertices in the activ region in the current realization and the
        # possible vertex. For every vertex in this union, we make a check
        # if the there are dangling vertices. If there are, we add the
        # vertex to a new set. If this set is in fact the possible active
        # region, we pass this validation.

        assert isinstance(realization, CutRealization)
        possible_active_region   = realization.get_active_vertices()
        union_active_region = self.get_active_vertices() | OrderedSet([possible_vertex])
        expected_active_region = OrderedSet()

        for vertex in union_active_region:
            if len(realization.dangling_vertices(vertex)) != 0:
                expected_active_region.add(vertex)
        
        return possible_active_region == expected_active_region

    def extend_vertex(self, possible_vertex):
        if not self.can_extend_vertex(possible_vertex):
            return False

        # Every time we extend a possible vertex, we should
        # find the maximal right end from all the right ends
        # in the interval. In order to make an extension, we
        # need to make a shift by the average value of the range
        # we define the intervals, in our case, this is 0.5.
        # We make a shift by this value and the maximal right value.

        max_right_value = next(
            self.get_interval_by_vertex(v).right_element
            for v in self.get_maximal_set()
        )
        interval_shift = max_right_value + 0.5

        # For all the active vertices in the current
        # realization, we shift thr right end of the
        # interval by from the already shifted value
        # variable.

        for active_vertex in self.get_active_vertices():
            interval = self.get_interval_by_vertex(active_vertex)
            assert isinstance(interval, Interval)
            interval.right_element = interval_shift + 1

        # When we have extended the active vertices, we add the possible
        # vertex corresponding interval in the interval set in the
        # current realization. We preserve the difference of 1 between
        # left end of the interval and the right end of the interval.

        self.domain_vertex.append(possible_vertex)
        self.intervals.append(Interval(possible_vertex, interval_shift, interval_shift + 1))
        self.domain_set.add(possible_vertex)

        # After we have done the extension of the current
        # vertex, we make evertyhing to emty / None for
        # possible next caculations and operations.

        self.__cached_active_vertices = None
        self.__cached_maximal_set = None
        self.__cached_dangling_set = None
        self.__cached_vertex_degree = {}
        return True
