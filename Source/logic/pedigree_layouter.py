# This Python file uses the following encoding: UTF-8

"""The module has the classes Shape, Line and Layout.

This module contains the logic of creating a layout of the
individuals in a given pedigree, based on its intervals.
"""

from functools import reduce
from typing import Union
from collections import defaultdict
from collections import OrderedDict

from logic.pedigree_units import Individual
from logic.pedigree_units import MatingUnit
from logic.pedigree_units import SibshipUnit

from logic.pedigree_problem import VertexInterval


class Shape:
    """Shape Class.

    This class is used to manage a
    shape associated to an individual.
    """

    def __init__(self, individual: Individual, x_coordinate=0.0, y_coordinate=0.0) -> None:
        """Initialize an instance of the Shape class.

        It accepts the individual and (X, Y) coordinates.
        """
        self.__individual = individual
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__size = 21.0
        self.__scale = 1.0

    @property
    def individual(self) -> Individual:
        """Return the individual property of the class."""
        return self.__individual

    @property
    def x_coordinate(self) -> float:
        """Return the x coordinate property of the class."""
        return self.__x_coordinate

    @property
    def y_coordinate(self) -> float:
        """Return the y coordinate property of the class."""
        return self.__y_coordinate

    @property
    def size(self) -> float:
        """Return the size property of the class."""
        return self.__size

    @property
    def scale(self) -> float:
        """Return the scale property of the class."""
        return self.__scale

    @property
    def x_center(self) -> float:
        """Return the x center property of the class."""
        return self.x_coordinate + self.size / 2.0

    @property
    def y_center(self) -> float:
        """Return the y coordinate property of the class."""
        return self.y_coordinate + self.size / 2.0

    @x_coordinate.setter
    def x_coordinate(self, x_coordinate: float) -> None:
        assert isinstance(x_coordinate, float)
        self.__x_coordinate = x_coordinate

    @y_coordinate.setter
    def y_coordinate(self, y_coordinate) -> None:
        assert isinstance(y_coordinate, float)
        self.__y_coordinate = y_coordinate

    def __repr__(self) -> str:
        """Return the string representation of the class."""
        return '(' + str(self.x_coordinate) + ',' + str(self.y_coordinate) + ')'


class Line:
    """Line Class.

    This class is used to manage a
    line connecting the shapes.
    """

    def __init__(self, x1_coordinate: float, y1_coordinate: float,
                 x2_coordinate: float, y2_coordinate: float) -> None:
        """Initialize an instance of the Line class.

        It accepts the (X1, Y1) endpoint and the (X2, Y2) endpoint.
        """
        self.__x1_coordinate = x1_coordinate
        self.__y1_coordinate = y1_coordinate
        self.__x2_coordinate = x2_coordinate
        self.__y2_coordinate = y2_coordinate

    @property
    def x1_coordinate(self) -> float:
        """Return the x1 coordinate property of the class."""
        return self.__x1_coordinate

    @property
    def y1_coordinate(self) -> float:
        """Return the y1 coordinate property of the class."""
        return self.__y1_coordinate

    @property
    def x2_coordinate(self) -> float:
        """Return the x2 coordinate property of the class."""
        return self.__x2_coordinate

    @property
    def y2_coordinate(self) -> float:
        """Return the y2 coordinate property of the class."""
        return self.__y2_coordinate

    @x1_coordinate.setter
    def x1_coordinate(self, x1_coordinate: float) -> None:
        assert isinstance(x1_coordinate, float)
        self.__x1_coordinate = x1_coordinate

    @y1_coordinate.setter
    def y1_coordinate(self, y1_coordinate: float) -> None:
        assert isinstance(y1_coordinate, float)
        self.__y1_coordinate = y1_coordinate

    @y2_coordinate.setter
    def y2_coordinate(self, y2_coordinate: float) -> None:
        assert isinstance(y2_coordinate, float)
        self.__y2_coordinate = y2_coordinate

    @x2_coordinate.setter
    def x2_coordinate(self, x2_coordinate: float) -> None:
        assert isinstance(x2_coordinate, float)
        self.__x2_coordinate = x2_coordinate

    def __repr__(self) -> str:
        """Return the string representation of the class."""
        return '[(' + str(self.x1_coordinate) + ',' + str(self.y1_coordinate) + \
            ') - (' + str(self.x2_coordinate) + ',' + str(self.y2_coordinate) + ')]'


class Layout:
    """Layout Class.

    This class is used to manage the
    creating of a layout of a pedigree.
    """

    def __init__(self, intervals: list) -> None:
        """Initialize an instance of the Layout class.

        It accepts the intervals of a given pedigree.
        """
        self.__intervals = intervals
        self.__lines = []
        self.__positions = []

        self.__individuals_intervals = self.split_intervals()[0]
        self.__mating_units_intervals = self.split_intervals()[1]
        self.__sibship_units_intervals = self.split_intervals()[2]

        self.__divided_individuals_by_rank = self.split_individuals_by_generation_rank()[0]
        self.__divided_mating_units_by_rank = self.split_mating_units_by_generation_rank()[0]
        self.__divided_sibship_units_by_rank = self.split_sibship_units_by_generation_rank()[0]

        self.__divided_individuals_intervals_by_rank = self.split_individuals_by_generation_rank()[1]
        self.__divided_mating_units_intervals_by_rank = self.split_mating_units_by_generation_rank()[1]
        self.__divided_sibship_units_intervals_by_rank = self.split_sibship_units_by_generation_rank()[1]

        self.__individuals_positions = self.generate_individuals_positions()
        self.generate_layout()

    @property
    def intervals(self) -> list:
        """Return the intervals property of the class."""
        return self.__intervals

    @property
    def lines(self) -> list:
        """Return the lines property of the class."""
        return self.__lines

    @property
    def positions(self) -> list:
        """Return the positions property of the class."""
        return self.__positions

    @property
    def individuals_intervals(self) -> list:
        """Return the individuals intervals property of the class."""
        return self.__individuals_intervals

    @property
    def mating_units_intervals(self) -> list:
        """Return the mating units intervals property of the class."""
        return self.__mating_units_intervals

    @property
    def sibship_units_intervals(self) -> list:
        """Return the sibship units intervals property of the class."""
        return self.__sibship_units_intervals

    @property
    def divided_individuals_by_rank(self):
        """Return the divided individuals by rank property of the class."""
        return self.__divided_individuals_by_rank

    @property
    def divided_mating_units_by_rank(self):
        """Return the divided mating units by rank property of the class."""
        return self.__divided_mating_units_by_rank

    @property
    def divided_sibship_units_by_rank(self):
        """Return the divided sibship units by rank property of the class."""
        return self.__divided_sibship_units_by_rank

    @property
    def divided_individuals_intervals_by_rank(self):
        """Return the divided individuals intervals by rank property of the class."""
        return self.__divided_individuals_intervals_by_rank

    @property
    def divided_mating_units_intervals_by_rank(self):
        """Return the divided mating units intervals by rank property of the class."""
        return self.__divided_mating_units_intervals_by_rank

    @property
    def divided_sibship_units_intervals_by_rank(self):
        """Return the divided sibship units intervals by rank property of the class."""
        return self.__divided_sibship_units_intervals_by_rank

    @property
    def individuals_positions(self):
        """Return the individuals positions property of the class."""
        return self.__individuals_positions

    def split_intervals(self) -> tuple:
        """Split the intervals by the generation ranks of the vertices.

        This method splits all the intervals by the generation ranks
        of the vertices. The intervals are divided in three different
        lists - one for the individual intervals, one for the mating
        units intervals and one for the sibship units intervals.
        """
        individuals_intervals = []
        mating_units_intervals = []
        sibship_units_intervals = []

        for interval in self.intervals:
            assert isinstance(interval, VertexInterval)

            if isinstance(interval.vertex, Individual):
                individuals_intervals.append(interval)
            elif isinstance(interval.vertex, MatingUnit):
                mating_units_intervals.append(interval)
            elif isinstance(interval.vertex, SibshipUnit):
                sibship_units_intervals.append(interval)
            else:
                raise Exception('Something went wrong!')

        return individuals_intervals, mating_units_intervals, sibship_units_intervals

    def split_individuals_by_generation_rank(self) -> tuple:
        """Split the individuals by generation rank.

        This method splits the individuals and their
        corresponding intervals by their generation rank.
        """
        divided_individuals_by_rank = []
        divided_intervals_by_rank = defaultdict(list)

        for individual_interval in self.__individuals_intervals:
            assert isinstance(individual_interval, VertexInterval)
            assert isinstance(individual_interval.vertex, Individual)
            generation_rank = individual_interval.vertex.generation_rank
            divided_intervals_by_rank[generation_rank].append(individual_interval)

        dictionary_keys = sorted(divided_intervals_by_rank.keys())

        for key in dictionary_keys:
            sorted_intervals = sorted(
                divided_intervals_by_rank[key],
                key=lambda x: (
                    x.left_element,
                    x.right_element
                )
            )

            interval_vertices = []

            for interval in sorted_intervals:
                assert isinstance(interval, VertexInterval)
                interval_vertices.append(interval.vertex)

            divided_individuals_by_rank.append(interval_vertices)

        divided_intervals_by_rank = sorted(divided_intervals_by_rank.items(), key=lambda x: x[0])
        divided_intervals_by_rank = OrderedDict(divided_intervals_by_rank)
        return divided_individuals_by_rank, divided_intervals_by_rank

    def split_mating_units_by_generation_rank(self) -> tuple:
        """Split the mating units by generation rank.

        This method splits the mating units and their
        corresponding intervals by their generation rank.
        """
        divided_mating_units_intervals = []
        divided_intervals_by_ranks = defaultdict(list)

        for mating_unit_interval in self.__mating_units_intervals:
            assert isinstance(mating_unit_interval, VertexInterval)
            assert isinstance(mating_unit_interval.vertex, MatingUnit)
            generation_rank = mating_unit_interval.vertex.generation_rank
            divided_intervals_by_ranks[generation_rank].append(mating_unit_interval)

        dictionary_keys = sorted(divided_intervals_by_ranks.keys())

        for key in dictionary_keys:
            sorted_intervals = sorted(
                divided_intervals_by_ranks[key],
                key=lambda x: (
                    x.left_element,
                    x.right_element
                )
            )

            interval_vertices = []

            for interval in sorted_intervals:
                assert isinstance(interval, VertexInterval)
                interval_vertices.append(interval.vertex)

            divided_mating_units_intervals.append(interval_vertices)

        divided_intervals_by_ranks = OrderedDict(sorted(divided_intervals_by_ranks.items(), key=lambda x: x[0]))
        return divided_mating_units_intervals, divided_intervals_by_ranks

    def split_sibship_units_by_generation_rank(self) -> tuple:
        """Split the sibship units by generation rank.

        This method splits the sibship units and their
        corresponding intervals by their generation rank.
        """
        divided_sibship_units_intervals = []
        divided_intervals_by_ranks = defaultdict(list)

        for sibship_unit_interval in self.__sibship_units_intervals:
            assert isinstance(sibship_unit_interval, VertexInterval)
            assert isinstance(sibship_unit_interval.vertex, SibshipUnit)
            generation_rank = sibship_unit_interval.vertex.generation_rank
            divided_intervals_by_ranks[generation_rank].append(sibship_unit_interval)

        dictionary_keys = sorted(divided_intervals_by_ranks.keys())

        for key in dictionary_keys:
            sorted_intervals = sorted(
                divided_intervals_by_ranks[key],
                key=lambda x: (
                    x.left_element,
                    x.right_element
                )
            )

            interval_vertices = []

            for interval in sorted_intervals:
                assert isinstance(interval, VertexInterval)
                interval_vertices.append(interval.vertex)

            divided_sibship_units_intervals.append(interval_vertices)

        divided_intervals_by_ranks = OrderedDict(sorted(divided_intervals_by_ranks.items(), key=lambda x: x[0]))
        return divided_sibship_units_intervals, divided_intervals_by_ranks

    def generate_individuals_positions(self):
        """Generate positions of the individuals in the canvas.

        This method generates a layout for the individuals in the canvas
        by sorting them according to their generation rank. It just
        draws them in a single line for every generation, while every
        first individual in the generation horizontally is one above
        another one.
        """
        individuals_positions = {}

        level_height = 30.0
        y_offset = 20.0
        gap = 8.0

        for rank, individuals in enumerate(self.divided_individuals_by_rank):
            x_offset = 20.0
            for individual in individuals:
                position = Shape(
                    individual, x_offset, y_offset + (rank + 1) * level_height
                )
                individuals_positions[individual] = position
                x_offset += position.size + gap

        return individuals_positions

    def generate_layout(self):
        """Generate the layout of a pedigree."""
        self.optimize_drawing()
        self.build_positioned_individuals()
        self.build_lines()

    def optimize_drawing(self):
        """Optimize the drawing of a pedigree.

        This method optimizes the drawing of a
        pedigree by moving the individuals to
        their possible right places by aligning
        parents to their children or children to
        their parents in the layout.
        """
        moved_individuals = -1
        counter = 1

        while moved_individuals and counter < 100:
            moved_individuals = 0
            if counter % 6 < 3:
                moved_individuals += self.align_parents_of_children()
                moved_individuals += self.align_children_of_parents()
            else:
                moved_individuals += self.align_children_of_parents()
                moved_individuals += self.align_parents_of_children()

            moved_individuals += self.move_overlaps()

            counter += 1
        self.align_left()

    def align_parents_of_children(self):
        """Align parents of children in the canvas."""
        moved_individuals = 0

        for level in reversed(self.divided_individuals_by_rank):
            sibship_groups = self.get_sibships_on_level(level)
            for sibship in sibship_groups:
                moved_individuals += self.center_parents_of_children(sibship)

        return moved_individuals

    def align_children_of_parents(self):
        """Align the children of parents in the canvas."""
        moved_individuals = 0

        for level in self.divided_individuals_by_rank:
            mating_units = self.get_matings_on_level(level)
            for mates in mating_units:
                moved_individuals += self.center_children_of_parents(mates)

        return moved_individuals

    @staticmethod
    def get_sibships_on_level(level: list) -> list:
        """Get all the sibships on a given level."""
        individuals_with_parents = []

        for individual in level:
            assert isinstance(individual, Individual)
            if individual.has_parents():
                individuals_with_parents.append(individual)

        def reducer(acc, instance):
            """Reduce individuals by a check with are_siblings."""
            assert isinstance(acc, list)
            assert isinstance(instance, Individual)

            if len(acc) == 0:
                return [[instance]]

            last_array = acc[len(acc) - 1]
            assert isinstance(last_array, list)

            if instance.are_siblings(last_array[0]):
                last_array.append(instance)
            else:
                acc.append([instance])

            return acc

        return reduce(reducer, individuals_with_parents, [])

    @staticmethod
    def get_matings_on_level(level: list) -> set:
        """Get all the matings on a given level."""
        result = set()

        for individual in level:
            assert isinstance(individual, Individual)

            for mating_unit in individual.mating_instances:
                result.add(mating_unit)

        return result

    def center_children_of_parents(self, mating_unit: MatingUnit) -> int:
        """Center children of parents in the canvas."""
        assert isinstance(mating_unit, MatingUnit)

        children = self.get_first_and_last_children_positions(mating_unit)
        assert isinstance(children[0], Shape)
        assert isinstance(children[1], Shape)
        children_center = (children[0].x_coordinate + children[1].x_coordinate) / 2.0

        father = self.individuals_positions[mating_unit.male_mate_individual]
        mother = self.individuals_positions[mating_unit.female_mate_individual]
        assert isinstance(father, Shape)
        assert isinstance(mother, Shape)

        parents_center = (father.x_coordinate + mother.x_coordinate) / 2.0
        offset = parents_center - children_center
        return self.move(children, offset)

    def center_parents_of_children(self, sibship: list) -> int:
        """Center parents of children in the canvas."""
        assert len(sibship) > 0
        some_child = sibship[0]

        assert isinstance(some_child, Individual)
        assert isinstance(self.individuals_positions[some_child], Shape)
        assert isinstance(self.individuals_positions[sibship[len(sibship) - 1]], Shape)

        start_x = self.individuals_positions[some_child].x_coordinate
        end_x = self.individuals_positions[sibship[len(sibship) - 1]].x_coordinate

        children_center = (start_x + end_x) / 2.0

        father = some_child.get_father_individual()
        mother = some_child.get_mother_individual()

        father_position = self.individuals_positions[father]
        mother_position = self.individuals_positions[mother]
        assert isinstance(father_position, Shape)
        assert isinstance(mother_position, Shape)

        ordered_parents = [mother_position, father_position]
        if father_position.x_coordinate < mother_position.x_coordinate:
            ordered_parents = [father_position, mother_position]

        parents_center = (father_position.x_coordinate + mother_position.x_coordinate) / 2.0
        offset = children_center - parents_center

        if offset > 0:
            return self.move(ordered_parents[1:], offset)
        return self.move(ordered_parents[0:1], offset)

    def move_overlaps(self) -> int:
        """Move overlaps in the canvas of the draw."""
        moved_individuals = 0
        first_individual_position = self.individuals_positions[
            self.divided_individuals_by_rank[0][0]
        ]
        assert isinstance(first_individual_position, Shape)
        min_gap = first_individual_position.size + 8.0

        for level in self.divided_individuals_by_rank:
            level_with_positions = [self.individuals_positions[i] for i in level]

            for index, individual1 in enumerate(level_with_positions):
                for individual2 in level_with_positions[index + 1: index + 2]:
                    assert isinstance(individual1, Shape)
                    assert isinstance(individual2, Shape)
                    difference = individual2.x_coordinate - individual1.x_coordinate

                    if min_gap - difference > 1:
                        moved_individuals += self.move([individual2], min_gap - difference)

        return moved_individuals

    def move(self, individuals: list, offset: float, already_moved=None) -> int:
        """Move the shapes of the individuals in the canvas.

        This method move the shapes of the individuals, given in a list
        by an offset, given as an argument. If there are already moved
        individuals, they are removed in the beginning and removed in the
        end of the method itself.
        """
        if already_moved is None:
            already_moved = set()

        assert len(individuals) > 0

        if abs(offset) < 1e-5:
            return 0

        individuals = list(set(individuals) - already_moved)

        min_individual = reduce(
            lambda a, b: a if a.x_coordinate < b.x_coordinate else b, individuals
        )
        max_individual = reduce(
            lambda a, b: a if a.x_coordinate > b.x_coordinate else b, individuals
        )

        assert isinstance(max_individual, Shape)
        assert isinstance(min_individual, Shape)

        level = self.get_level_of_individual(min_individual.individual)

        individuals = level[
            level.index(min_individual.individual): level.index(
                max_individual.individual
            ) + 1
        ]
        individuals = [self.individuals_positions[x] for x in individuals]
        individuals = list(set(individuals) - already_moved)

        if len(individuals) == 0:
            return 0

        to_move_offset = 0

        start = min_individual.x_coordinate
        end = max_individual.x_coordinate
        to_move = set()

        if offset > 0:
            new_end = end + offset

            for element in level:
                for i in [self.individuals_positions[element]]:
                    assert isinstance(i, Shape)
                    if start <= i.x_coordinate <= new_end:
                        to_move.add(i)

            to_move -= already_moved
            to_move -= set(individuals)

            if len(to_move) != 0:
                to_move_offset = max(
                    [new_end - i.x_coordinate + 8.0 * 2.0 + i.size for i in to_move]
                )
        else:
            new_start = start + offset

            for element in level:
                for i in [self.individuals_positions[element]]:
                    assert isinstance(i, Shape)
                    if start <= i.x_coordinate <= new_start:
                        to_move.add(i)

            to_move -= already_moved
            to_move -= set(individuals)

            if len(to_move) != 0:
                to_move_offset = min(
                    [new_start - i.x_coordinate - 8.0 * 2.0 - i.size for i in to_move]
                )

        for individual in individuals:
            assert isinstance(individual, Shape)
            individual.x_coordinate += offset

        other_moved = 0
        if len(to_move) != 0:
            other_moved = self.move(
                list(to_move), to_move_offset, already_moved | set(individuals)
            )

        return len(individuals) + other_moved

    def align_left(self) -> None:
        """Align left the positions the individuals in the layout.

        This method align to the left direction the positions of
        all the individuals in the pedigree layout with their shapes.
        """
        min_x = min([i.x_coordinate for i in list(self.individuals_positions.values())])

        for individual in list(self.individuals_positions.values()):
            assert isinstance(individual, Shape)
            individual.x_coordinate = individual.x_coordinate - min_x + 10.0

    def get_first_and_last_children_positions(self, mating_unit: MatingUnit) -> list:
        """Get the position of the first and the last children of a mating unit."""
        assert isinstance(mating_unit, MatingUnit)
        assert isinstance(mating_unit.sibship_unit_relation, SibshipUnit)
        children = mating_unit.sibship_unit_relation.siblings_individuals

        children_positions = [self.individuals_positions[x] for x in children]
        children_positions = sorted(children_positions, key=lambda x: x.x_coordinate)

        return [
            children_positions[0],
            children_positions[len(children_positions) - 1],
        ]

    def get_level_of_individual(self, individual: Individual) -> Union[list, None]:
        """Get the corresponding level of an individual."""
        for individuals_on_level in self.divided_individuals_by_rank:
            if individual in individuals_on_level:
                return individuals_on_level

        return None

    def build_positioned_individuals(self):
        """Build the positioned individuals in the layout."""
        for level in self.divided_individuals_by_rank:
            self.positions.append([self.individuals_positions[x] for x in level])

    def build_lines(self):
        """Build all the lines connecting in the canvas.

        This method builds all the lines connecting the
        individuals, the mating units and the sibship units
        in the layout of the pedigree.
        """
        for level in self.positions:
            for start, individual in enumerate(level):
                assert isinstance(individual, Shape)
                assert isinstance(individual.individual, Individual)

                if individual.individual.mating_unit_relation:
                    self.lines.append(
                        Line(
                            individual.x_center,
                            individual.y_coordinate,
                            individual.x_center,
                            individual.y_center - 15,
                        )
                    )

                for i, other_individual in enumerate(level[start + 1:]):
                    are_next_to_each_other = (i == 0)
                    assert isinstance(other_individual, Shape)

                    if individual.individual.are_mates(other_individual.individual):
                        middle_x = (individual.x_center + other_individual.x_center) / 2.0

                        if are_next_to_each_other:
                            self.lines.append(
                                Line(
                                    individual.x_coordinate + individual.size,
                                    individual.y_center,
                                    other_individual.x_coordinate,
                                    other_individual.y_center,
                                )
                            )
                            self.lines.append(
                                Line(
                                    middle_x,
                                    individual.y_center,
                                    middle_x,
                                    individual.y_center + 15,
                                )
                            )
                            continue

            i = 0
            while i < len(level) - 1:
                j = len(level) - 1
                while i < j:
                    individual = level[i]
                    other_individual = level[j]

                    assert isinstance(individual, Shape)
                    assert isinstance(other_individual, Shape)

                    if individual.individual.are_siblings(other_individual.individual):
                        self.lines.append(
                            Line(
                                individual.x_center,
                                individual.y_center - 15,
                                other_individual.x_center,
                                other_individual.y_center - 15,
                            )
                        )
                        i = j
                        break
                    j -= 1
                i += 1
