from re import I
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

from collections import defaultdict
from matplotlib.backends.backend_pdf import PdfPages

from family_units import Individual
from family_units import MatingUnit
from family_units import SibshipUnit
from interval_sandwich import Interval
from fields import Sex, Status


class Drawer:
    def __init__(self, pedigree_identifier, pedigree_intervals):
        self.__pedigree_identifier      =   pedigree_identifier
        self.__pedigree_intervals       =   pedigree_intervals

        self.__individuals_intervals    =   self.find_individuals_intervals()
        self.__mating_units_intervals   =   self.find_mating_units_intervals()
        self.__sibship_units_intervals  =   self.find_sibship_units_intervals()

        self.__splitted_individuals_by_ranks        =   self.split_individuals_by_generation_ranks()
        self.__splitted_mating_units_by_ranks       =   self.split_mating_units_by_generation_ranks()
        self.__splitted_sibship_units_by_ranks      =   self.split_sibship_units_by_generation_ranks()

        self.__coordinated_individuals               =   self.draw_individual_coordinates()
        self.draw_file()


    @property
    def pedigree_identifier(self):
        return self.__pedigree_identifier

    
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


    @property
    def splitted_individuals_by_ranks(self):
        return self.__splitted_individuals_by_ranks


    @property
    def splitted_mating_units_by_ranks(self):
        return self.__splitted_mating_units_by_ranks


    @property
    def splitted_sibship_units_by_ranks(self):
        return self.__splitted_sibship_units_by_ranks


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


    @pedigree_identifier.deleter
    def pedigree_idengifier(self):
        del self.__pedigree_identifier


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


    @splitted_individuals_by_ranks.deleter
    def splitted_individuals_by_ranks(self):
        del self.__splitted_individuals_by_ranks


    @splitted_mating_units_by_ranks.deleter
    def splitted_mating_units_by_ranks(self):
        del self.__splitted_mating_units_by_ranks


    @splitted_sibship_units_by_ranks.deleter
    def splitted_sibship_units_by_ranks(self):
        del self.__splitted_sibship_units_by_ranks


    def __del__(self):
        del self.__pedigree_identifier
        del self.__pedigree_intervals
        del self.__individuals_intervals
        del self.__mating_units_intervals
        del self.__sibship_units_intervals
        del self.__splitted_individuals_by_ranks
        del self.__splitted_mating_units_by_ranks
        del self.__splitted_sibship_units_by_ranks


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


    def draw_individual_coordinates(self):
        coordinated_individuals = dict()

        x_axis_offset   =   50
        y_axis_offset   =   50
        distance_offset =   50
        height_offset   =   50
        
        for i in range(len(self.__splitted_individuals_by_ranks)):
            generation_rank = i
            x_axis_offset = 50

            for individual in self.__splitted_individuals_by_ranks[i]:
                positions = IndividualDrawer(individual,
                    x_axis_offset, generation_rank * height_offset + y_axis_offset
                )
                coordinated_individuals[individual] = positions
                x_axis_offset = x_axis_offset + 30.0 + distance_offset

        return coordinated_individuals


    def draw_file(self):
        axes = plt.figure().add_subplot(111)

        for individual in self.__coordinated_individuals:
            print(individual)
            position = self.__coordinated_individuals[individual]
            assert isinstance(position, IndividualDrawer)
            assert isinstance(position.individual, Individual)

            x_position = position.x_coordinate
            y_position = position.y_coordinate

            if position.individual.individual_sex is Sex.MALE:
                if position.individual.individual_status is Status.AFFECTED:
                    axes.add_patch(Rectangle((x_position, y_position), 30, 30, edgecolor='black', facecolor='red'))
                    plt.text(x_position - 15, y_position + 15, str(position.individual.individual_identifier))
                elif position.individual.individual_status is Status.UNAFFECTED:
                    axes.add_patch(Rectangle((x_position, y_position), 30, 30, edgecolor='black', facecolor='white'))
                    plt.text(x_position - 15, y_position + 15, str(position.individual.individual_identifier))
                else:
                    axes.add_patch(Rectangle((x_position, y_position), 30, 30, edgecolor='black', facecolor='gray'))
                    plt.text(x_position - 15, y_position + 15, str(position.individual.individual_identifier))
            elif position.individual.individual_sex is Sex.FEMALE:
                if position.individual.individual_status is Status.AFFECTED:
                    axes.add_patch(Circle((x_position + 15, y_position + 15), 15, edgecolor='black', facecolor='red'))
                    plt.text(x_position - 7.5, y_position + 5, str(position.individual.individual_identifier))
                elif position.individual.individual_status is Status.UNAFFECTED:
                    axes.add_patch(Circle((x_position + 15, y_position + 15), 15, edgecolor='black', facecolor='white'))
                    plt.text(x_position - 7.5, y_position + 15, str(position.individual.individual_identifier))
                else:
                    axes.add_patch(Circle((x_position + 15, y_position + 15), 15, edgecolor='black', facecolor='gray'))
                    plt.text(x_position - 7.5, y_position + 15, str(position.individual.individual_identifier))

        for mating_unit_level in self.splitted_mating_units_by_ranks:
            for mating_unit in mating_unit_level:
                assert isinstance(mating_unit, MatingUnit)
                
                father = mating_unit.male_mate_individual
                mother = mating_unit.female_mate_individual

                if father and mother in self.__coordinated_individuals.keys():
                    father_position = self.__coordinated_individuals[father]
                    mother_position = self.__coordinated_individuals[mother]

                    assert isinstance(father_position, IndividualDrawer)
                    assert isinstance(mother_position, IndividualDrawer)

                    father_interval = None
                    mother_interval = None

                    for interval in self.__individuals_intervals:
                        assert isinstance(interval, Interval)
                        assert isinstance(interval.vertex, Individual)

                        if interval.vertex is father:
                            father_interval = [interval.left_element, interval.right_element]
                        elif interval.vertex is mother:
                            mother_interval = [interval.left_element, interval.right_element]

                        if father_interval is not None and mother_interval is not None:
                            break

                    x_values_horizontal_line = list()
                    y_values_horizontal_line = list()
                    x_values_vertical_line = list()
                    y_values_vertical_line = list()

                    if father_interval[1] < mother_interval[0]:    
                        x_values_horizontal_line = [father_position.x_coordinate + 30, mother_position.x_coordinate]
                        y_values_horizontal_line = [father_position.y_coordinate + 15, mother_position.y_coordinate + 15]
                    else:
                        x_values_horizontal_line = [mother_position.x_coordinate + 30, father_position.x_coordinate]
                        y_values_horizontal_line = [mother_position.y_coordinate + 15, father_position.y_coordinate + 15]

                    x_middle = (x_values_horizontal_line[1] - x_values_horizontal_line[0]) / 2.0 + x_values_horizontal_line[0]
                    
                    x_values_vertical_line = [x_middle, x_middle]
                    y_values_vertical_line = [y_values_horizontal_line[0], y_values_horizontal_line[0] + 20]

                    sibship_unit = mating_unit.sibship_unit_relation

                    if len(sibship_unit.siblings_individuals) > 1:
                        sibship_unit_span_x_vertical_line = [
                            x_values_vertical_line[1] - (len(sibship_unit.siblings_individuals) / 2.0) * 40,
                            x_values_vertical_line[1] + (len(sibship_unit.siblings_individuals) / 2.0) * 40
                        ]
                        sibship_unit_span_y_vertical_line = [y_values_vertical_line[1], y_values_vertical_line[1]]

                    plt.plot(x_values_horizontal_line, y_values_horizontal_line, color='black')
                    plt.plot(x_values_vertical_line, y_values_vertical_line, color='black')
                    plt.plot(sibship_unit_span_x_vertical_line, sibship_unit_span_y_vertical_line, color='black')

        plt.xlim([0, 300])
        plt.ylim([200, 0])

        plt.title(str(self.pedigree_identifier))
        plt.savefig(str(self.pedigree_identifier) + '.pdf')
        plt.show()

    
    def move_individual(self, individual):
        pass


class IndividualDrawer:
    def __init__(self, individual, x_coordinate, y_coordinate, size_shape = 30.0, scale_shape = 1.0):
        self.__individual       =   individual
        self.__x_coordinate     =   x_coordinate
        self.__y_coordinate     =   y_coordinate
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


    def move_individual(self, x_offset = 0.0, y_offset = 0.0):
        self.__x_coordinate = self.__x_coordinate + x_offset
        self.__y_coordinate = self.__y_coordinate + y_offset
        self.__x_center_shape = self.calculate_x_center()
        self.__y_center_shape = self.calculate_y_center()


class MatingUnitDrawer:
    def __init__(self, male_mate_drawer, female_mate_drawer):
        assert isinstance(male_mate_drawer, IndividualDrawer)
        assert isinstance(female_mate_drawer, IndividualDrawer)

        self.__male_mate_drawer     =   male_mate_drawer
        self.__female_mate_drawer   =   female_mate_drawer

        self.__mating_unit_span                 =   self.calculate_mating_unit_span()
        self.__mating_unit_span_length          =   self.calculate_mating_unit_span_length()
        self.__mating_unit_connection           =   self.calculate_mating_unit_connection()
        self.__mating_unit_connection_length    =   self.calculate_mating_unit_connection_length()


    @property
    def male_mate_drawer(self):
        return self.__male_mate_drawer


    @property
    def female_mate_drawer(self):
        return self.__female_mate_drawer


    @property
    def mating_unit_span(self):
        return self.__mating_unit_span


    @property
    def mating_unit_span_length(self):
        return self.__mating_unit_span_length


    @property
    def mating_unit_connection(self):
        return self.__mating_unit_connection


    @property
    def mating_unit_connection_length(self):
        return self.__mating_unit_connection_length

    
    def __del__(self):
        del self.__male_mate_drawer
        del self.__female_mate_drawer
        del self.__mating_unit_span
        del self.__mating_unit_span_length
        del self.__mating_unit_connection
        del self.__mating_unit_connection_length


    def calculate_mating_unit_span(self):
        x_coordinates = list()
        y_coordinates = list()

        if self.male_mate_drawer.x_center_shape < self.female_mate_drawer.x_center_shape:
            x_coordinates.append(self.male_mate_drawer.x_coordinate + 30.0)
            x_coordinates.append(self.female_mate_drawer.x_coordinate)
            y_coordinates.append(self.male_mate_drawer.y_coordinate + 15.0)
            y_coordinates.append(self.female_mate_drawer.y_coordinate + 15.0)
        else:
            x_coordinates.append(self.female_mate_drawer.x_coordinate + 30.0)
            x_coordinates.append(self.male_mate_drawer.x_coordinate)
            y_coordinates.append(self.male_mate_drawer.y_coordinate + 15.0)
            y_coordinates.append(self.female_mate_drawer.y_coordinate + 15.0)

        return [x_coordinates, y_coordinates]

    def calculate_mating_unit_connection(self):
        x_coordinates = list()
        y_coordinates = list()

        x_coordinates.append(self.__mating_unit_span[0][0] + self.__mating_unit_span_length / 2.0)
        x_coordinates.append(self.__mating_unit_span[0][0] + self.__mating_unit_span_length / 2.0)

        y_coordinates.append(self.__mating_unit_span[1][0])
        y_coordinates.append(self.__mating_unit_span[1][0] + 25.0)

        return [x_coordinates, y_coordinates]


    def calculate_mating_unit_span_length(self):
        return (self.__mating_unit_span[0][1] - self.__mating_unit_span[0][0])


    def calculate_mating_unit_connection_length(self):
        return (self.__mating_unit_connection[1][1] - self.__mating_unit_connection[1][0])


    def move_mating_unit(self, x_offset = 0.0, y_offset = 0.0):
        self.__male_mate_drawer.move_individual(x_offset)
        self.__female_mate_drawer.move_individual(y_offset)


    def mirror_mating_unit(self):
        if self.__male_mate_drawer.x_center_shape < self.__female_mate_drawer.x_center_shape:
            self.__male_mate_drawer.move_individual(60, 0)
            self.__female_mate_drawer.move_individual(-60, 0) 
        else:
            self.__male_mate_drawer.move_individual(-60, 0)
            self.__female_mate_drawer.move_individual(60, 0)


class SibshipUnitDrawer:
    def __init__(self, siblings_drawers):
        assert isinstance(siblings_drawers, list)

        self.__siblings_drawers                 =   siblings_drawers
        self.__sibship_unit_span                =   self.calculate_sibship_unit_span()
        self.__sibship_unit_span_length         =   None
        self.__sibship_unit_connection          =   self.calculate_sibship_unit_connection()
        self.__sibship_unit_connection_lenght   =   None


    def __del__(self):
        del self.__siblings_drawers
        del self.__sibship_unit_span
        del self.__sibship_unit_connection


    def calculate_sibship_unit_span(self):
        pass


    def calculate_sibship_unit_connection(self):
        pass
