import matplotlib.pyplot as plt


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

        self.split_individuals_by_generation_ranks()
        self.split_mating_units_by_generation_ranks()
        self.split_sibship_units_by_generation_ranks()


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

        dictionary_keys = sorted(splitted_intervals_by_ranks)

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

        print(splitted_individuals_intervals)
        return splitted_individuals_intervals


    def split_mating_units_by_generation_ranks(self):
        splitted_mating_units_intervals = list()
        splitted_intervals_by_ranks = defaultdict(list)

        for mating_unit_interval in self.__mating_units_intervals:
            assert isinstance(mating_unit_interval, Interval)
            assert isinstance(mating_unit_interval.vertex, MatingUnit)
            generation_rank = mating_unit_interval.vertex.generation_rank
            splitted_intervals_by_ranks[generation_rank].append(mating_unit_interval)

        dictionary_keys = sorted(splitted_intervals_by_ranks)

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

        print(splitted_mating_units_intervals)
        return splitted_mating_units_intervals


    def split_sibship_units_by_generation_ranks(self):
        splitted_sibship_units_intervals = list()
        splitted_intervals_by_ranks = defaultdict(list)
        
        for sibship_unit_interval in self.__sibship_units_intervals:
            assert isinstance(sibship_unit_interval, Interval)
            assert isinstance(sibship_unit_interval.vertex, SibshipUnit)
            generation_rank = sibship_unit_interval.vertex.generation_rank
            splitted_intervals_by_ranks[generation_rank].append(sibship_unit_interval)

        dictionary_keys = sorted(splitted_intervals_by_ranks)

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

        print(splitted_sibship_units_intervals)
        return splitted_sibship_units_intervals
