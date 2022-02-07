from re import I
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages


from collections import defaultdict


from FamilyUnits import Individual
from FamilyUnits import MatingUnit
from FamilyUnits import SibshipUnit
from IntervalSandwich import Interval


class Drawer:
    def __init__(self, intervals):
        self.__pedigree_intervals       =   intervals

        self.__individuals_intervals    =   self.find_individuals_intervals()
        self.__mating_units_intervals   =   self.find_mating_units_intervals()
        self.__sibship_units_intervals  =   self.find_sibship_units_intervals()

        self.__splitted_individuals_by_ranks        =   self.split_individuals_by_generation_ranks()
        self.__splitted_mating_units_by_ranks       =   self.split_mating_units_by_generation_ranks()
        self.__splitted_sibship_units_by_ranks      =   self.split_sibship_units_by_generation_ranks()

        self.__pedigree_positions                   =   self.draw_pedigree_positions()


    @property
    def pedigree_intervals(self):
        return self.__pedigree_intervals


    @property
    def individuals_intervals(self):
        return self.__individuals_intervals


    @property
    def mating_units_intervals(self):
        return self.__mating_units_intervals


    @property
    def sibship_units_intervals(self):
        return self.__sibship_units_intervals


    @pedigree_intervals.setter
    def pedigree_intervals(self, pedigree_intervals):
        self.__pedigree_intervals = pedigree_intervals


    @individuals_intervals.setter
    def individuals_intervals(self, individuals_intervals):
        self.__individuals_intervals = individuals_intervals


    @mating_units_intervals.setter
    def mating_units_intervals(self, mating_units_intervals):
        self.__mating_units_intervals = mating_units_intervals


    @sibship_units_intervals.setter
    def sibship_units_intervals(self, sibship_units_intervals):
        self.__sibship_units_intervals = sibship_units_intervals


    @pedigree_intervals.deleter
    def intervals(self):
        del self.__pedigree_intervals


    @individuals_intervals.deleter
    def individuals_intervals(self):
        del self.__individuals_intervals


    @mating_units_intervals.deleter
    def mating_units_intervals(self):
        del self.__mating_units_intervals


    @sibship_units_intervals.deleter
    def sibship_units_intervals(self):
        del self.__sibship_units_intervals


    def __del__(self):
        del self.__pedigree_intervals
        del self.__individuals_intervals
        del self.__mating_units_intervals
        del self.__sibship_units_intervals


    def find_individuals_intervals(self):
        individuals_intervals = list()

        for interval in self.intervals:
            assert isinstance(interval, Interval)
            
            if isinstance(interval.vertex, Individual):
                individuals_intervals.append(interval)

        return individuals_intervals


    def find_mating_units_intervals(self):
        mating_units_intervals = list()

        for interval in self.pedigree_intervals:
            assert isinstance(interval, Interval)

            if isinstance(interval.vertex, MatingUnit):
                mating_units_intervals.append(interval)

        return mating_units_intervals


    def find_sibship_units_intervals(self):
        sibship_units_intervals = list()

        for interval in self.intervals:
            assert isinstance(interval, Interval)

            if isinstance(interval.vertex, SibshipUnit):
                sibship_units_intervals.append(interval)

        return sibship_units_intervals


    def split_individuals_by_generation_ranks(self):
        splitted_individuals_intervals = list()
        splitted_intervals_by_ranks = defaultdict(list)

        for individual_interval in self.__individuals_intervals:
            assert isinstance(individual_interval, Interval)
            assert isinstance(individual_interval.vertex, Individual)
            generation_rank = individual_interval.vertex.generation_rank
            splitted_intervals_by_ranks[generation_rank].append(individual_interval)

        dictionary_keys = sorted(splitted_intervals_by_ranks.keys())

        for key in dictionary_keys:
            sorted_intervals = sorted(
                splitted_intervals_by_ranks[key],
                key = lambda x: (
                    x.left_element,
                    x.right_element
                )
            )

            interval_vertices = list()

            for interval in sorted_intervals:
                assert isinstance(interval, Interval)
                interval_vertices.append(interval.vertex)

            splitted_individuals_intervals.append(interval_vertices)

        return splitted_individuals_intervals


    def split_mating_units_by_generation_ranks(self):
        splitted_mating_units_intervals = list()
        splitted_intervals_by_ranks = defaultdict(list)

        for mating_unit_interval in self.__mating_units_intervals:
            assert isinstance(mating_unit_interval, Interval)
            assert isinstance(mating_unit_interval.vertex, MatingUnit)
            generation_rank = mating_unit_interval.vertex.generation_rank
            splitted_intervals_by_ranks[generation_rank].append(mating_unit_interval)

        dictionary_keys = sorted(splitted_intervals_by_ranks.keys())

        for key in dictionary_keys:
            sorted_intervals = sorted(
                splitted_intervals_by_ranks[key],
                key = lambda x: (
                    x.left_element,
                    x.right_element
                )
            )

            interval_vertices = list()

            for interval in sorted_intervals:
                assert isinstance(interval, Interval)
                interval_vertices.append(interval.vertex)

            splitted_mating_units_intervals.append(interval_vertices)

        return splitted_mating_units_intervals


    def split_sibship_units_by_generation_ranks(self):
        splitted_sibship_units_intervals = list()
        splitted_intervals_by_ranks = defaultdict(list)
        
        for sibship_unit_interval in self.__sibship_units_intervals:
            assert isinstance(sibship_unit_interval, Interval)
            assert isinstance(sibship_unit_interval.vertex, SibshipUnit)
            generation_rank = sibship_unit_interval.vertex.generation_rank
            splitted_intervals_by_ranks[generation_rank].append(sibship_unit_interval)

        dictionary_keys = sorted(splitted_intervals_by_ranks.keys())

        for key in dictionary_keys:
            sorted_intervals = sorted(
                splitted_intervals_by_ranks[key],
                key = lambda x: (
                    x.left_element,
                    x.right_element
                )
            )

            interval_vertices = list()

            for interval in sorted_intervals:
                assert isinstance(interval, Interval)
                interval_vertices.append(interval.vertex)

            splitted_sibship_units_intervals.append(interval_vertices)

        return splitted_sibship_units_intervals


    def draw_pedigree_positions(self):
        pedigree_positions = dict()

        x_axis_offset   =   20.0
        y_axis_offset   =   20.0
        distance_offset =    8.0
        height_distance =   30.0
        original_offset =   x_axis_offset

        for i in range(len(self.__splitted_individuals_by_ranks)):
            generation_rank = i + 1
            x_axis_offset = original_offset

            for individual in self.__splitted_individuals_by_ranks[i]:
                pedigree_positions[individual] = IndividualDrawer(
                    individual, x_axis_offset,
                    generation_rank * height_distance + y_axis_offset
                )
                x_axis_offset = x_axis_offset + 21.0 + distance_offset

        return pedigree_positions


class IndividualDrawer:
    def __init__(self, individual, x__coordinate, y__coordinate, size_shape = 21.0, scale_shape = 1.0):
        self.__individual       =   individual
        self.__x_coordinate     =   x__coordinate
        self.__y_coordinate     =   y__coordinate
        self.__size_shape       =   size_shape
        self.__scale_shape      =   scale_shape
        self.__x_center_shape   =   self.calculate_x_center()
        self.__y_center_shape   =   self.calculate_y_center()


    @property
    def individual(self):
        return self.__individual


    @property
    def x_coordinate(self):
        return self.__x_coordinate


    @property
    def y_coordinate(self):
        return self.__y_coordinate


    @property
    def size_shape(self):
        return self.__size_shape


    @property
    def scale_shape(self):
        return self.__scale_shape


    @property
    def x_center_shape(self):
        return self.__x_center_shape


    @property
    def y_center_shape(self):
        return self.__y_center_shape


    def calculate_x_center(self):
        return self.x_coordinate + self.size_shape / 2.0


    def calculate_y_center(self):
        return self.y_coordinate + self.size_shape / 2.0


    def __repr__(self):
        return  '(' + str(self.x_coordinate) + \
                ', ' + str(self.y_coordinate) + ')'


    def __del__(self):
        del self.__individual
        del self.__x_coordinate
        del self.__y_coordinate
        del self.__size_shape
        del self.__scale_shape
        del self.__x_center_shape
        del self.__y_center_shape


class PDFCreator:
    def __init__(self, filename):
        self.__filename     =   filename


    @property
    def filename(self):
        return self.__filename


    @filename.deleter
    def filename(self):
        del self.__filename


    def __del__(self):
        del self.__filename
