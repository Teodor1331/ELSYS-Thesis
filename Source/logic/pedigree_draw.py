# This Python file uses the following encoding: UTF-8

"""This module has the classes PDFBuilder and LayoutDrawer.

This module contains the logic of drawing the pedigree
according to a given layout from the same pedigree.
"""

from copy import deepcopy

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as col

from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib.backends.backend_pdf import PdfPages

from .pedigree_fields import Sex
from .pedigree_fields import Status
from .pedigree_fields import Role

from .pedigree_units import Individual

from .pedigree_layouter import Shape
from .pedigree_layouter import Line
from .pedigree_layouter import Layout


mpl.use("PS")
plt.ioff()


def validate_colors_statuses(dictionary_colors: dict) -> bool:
    """Validate the dictionary with colors of the statuses."""
    assert isinstance(dictionary_colors, dict)

    for color in dictionary_colors.items():
        if color[1] not in col.cnames:
            return False

    return True


class PDFBuilder:
    """PDFBuilder Class.

    This class is used to create a PDF file
    with exactly one page and plot a whole
    drawing of a pedigree in in the page.
    """

    def __init__(self, filename: str) -> None:
        """Initialize an instance of the PDFBuilder class.

        It accepts the filename of the PDF file.
        """
        self.__filename = filename
        self.__page = None

    @property
    def filename(self) -> str:
        """Return the filename property of the class."""
        return self.__filename

    @property
    def page(self) -> PdfPages:
        """Return the page property of the class."""
        return self.__page

    def __enter__(self) -> PdfPages:
        """Declare what happens in the start of a context manager block."""
        self.__page = PdfPages(self.filename)
        return self.page

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        """Declare what happens in the end of a content manager block."""
        self.page.close()


class LayoutDrawer:
    """LayoutDrawer Class.

    This class is used to create the drawing
    from a given layout of a given pedigree.
    """

    def __init__(self, layout: Layout, x_offset: int, y_offset: int, colors: dict, figsize=(7, 10)) -> None:
        """Initialize an instance of the LayoutDrawer class.

        It accepts an instance of the Layout class, two integer
        for the offset by X and Y axes, a dictionary with the colors
        for the individual statuses and the figure size.
        """
        try:
            assert isinstance(layout, Layout)
            assert isinstance(x_offset, int)
            assert isinstance(y_offset, int)
            assert not isinstance(colors, type(None))
        except AssertionError as assertion_error:
            message = 'The layout drawer constructor arguments are not correct!'
            raise AssertionError(message) from assertion_error

        self.__layout = deepcopy(layout)
        self.__x_offset = x_offset
        self.__y_offset = y_offset
        self.__figsize = figsize
        self.__colors = colors

        self.rotate_drawing()

    @property
    def layout(self) -> Layout:
        """Return the layout property of the class."""
        return self.__layout

    @property
    def x_offset(self) -> int:
        """Return the x offset property of the class."""
        return self.__x_offset

    @property
    def y_offset(self) -> int:
        """Return the y offset property of the class."""
        return self.__y_offset

    @property
    def figsize(self) -> tuple:
        """Return the figsize property of the class."""
        return self.__figsize

    @property
    def colors(self) -> dict:
        """Return the colors property of the class."""
        return self.__colors

    def draw(self, pedigree_name: str) -> mpl.figure.Figure:
        """Create the figure and draw the pedigree name in the file.

        This method creates the figure and initializes the axes
        of the plot in order to call the methods for plotting
        the lines and plotting the individuals in the file.
        """
        figure = plt.figure(figsize=self.figsize)
        pedigree_axes_rectangle = (0.1, 0.3, 0.8, 0.6)

        axes_pedigree = figure.add_axes(pedigree_axes_rectangle)
        axes_pedigree.axis("off")
        axes_pedigree.set_aspect(aspect="equal", adjustable="datalim", anchor="C")
        axes_pedigree.autoscale_view()

        figure.text(0.5, 0.9, pedigree_name, horizontalalignment="center")

        self.draw_individuals(axes_pedigree)
        self.draw_lines(axes_pedigree)

        axes_pedigree.plot()
        return figure

    def draw_individuals(self, axes: plt.Axes) -> None:
        """Draw individuals in the PDF file with their specifics.

        This method draws the individuals according to their
        positions from the layout. It draws them with their
        specifications for the sex and the status. Every
        individual is annotated with its unique identifier.
        """
        for level in self.layout.positions:
            for individual in level:
                assert isinstance(individual, Shape)
                assert isinstance(individual.individual, Individual)

                individual_color = None

                if individual.individual.individual_status == Status.UNKNOWN:
                    individual_color = self.colors['unknown']
                elif individual.individual.individual_status == Status.UNAFFECTED:
                    individual_color = self.colors['unaffected']
                elif individual.individual.individual_status == Status.AFFECTED:
                    individual_color = self.colors['affected']

                if individual.individual.individual_sex == Sex.MALE:
                    coordinates_rectangle = (
                        individual.x_coordinate + self.x_offset,
                        individual.y_coordinate + self.y_offset
                    )
                    axes.add_patch(
                        Rectangle(
                            coordinates_rectangle,
                            individual.size,
                            individual.size,
                            facecolor=individual_color,
                            edgecolor='black',
                        )
                    )

                    annotation_x = coordinates_rectangle[0] + individual.size / 2.0
                    annotation_y = coordinates_rectangle[1] + individual.size / 2.0

                else:
                    coordinates_circle = (
                        individual.x_center + self.x_offset,
                        individual.y_center + self.y_offset,
                    )
                    axes.add_patch(
                        Circle(
                            coordinates_circle,
                            individual.size / 2,
                            facecolor=individual_color,
                            edgecolor='black',
                        )
                    )

                    annotation_x = coordinates_circle[0]
                    annotation_y = coordinates_circle[1]

                if individual.individual.individual_role == Role.PROBAND:
                    axes.annotate(
                        individual.individual.individual_identifier,
                        (annotation_x, annotation_y),
                        color="black",
                        weight="bold",
                        style='italic',
                        fontsize=5,
                        ha="center",
                        va="center",
                    )
                else:
                    axes.annotate(
                        individual.individual.individual_identifier,
                        (annotation_x, annotation_y),
                        color="black",
                        weight="bold",
                        fontsize=5,
                        ha="center",
                        va="center",
                    )

    def draw_lines(self, axes: plt.Axes) -> None:
        """Draw lines in the PDF file for connecting the individuals.

        This method draws every single line needed for connecting
        the shapes of the individuals in the already plotted canvas.
        """
        for line in self.layout.lines:
            assert isinstance(line, Line)

            axes.add_line(
                Line2D(
                    [line.x1_coordinate + self.x_offset, line.x2_coordinate + self.x_offset],
                    [line.y1_coordinate + self.y_offset, line.y2_coordinate + self.y_offset],
                    color="black",
                )
            )

    def rotate_drawing(self) -> None:
        """Rotate the plotted drawing in the canvas.

        This method applies the needed rotation of the
        canvas with the plotted shapes of the individuals
        and the plotted lines connecting them in the drawing.
        """
        y_coordinates = []

        for level in self.layout.positions:
            for individual in level:
                assert isinstance(individual, Shape)
                y_coordinates.append(individual.y_coordinate)

        max_y_coordinate = max(y_coordinates) + 10

        for level in self.layout.positions:
            for individual in level:
                assert isinstance(individual, Shape)
                individual.y_coordinate = max_y_coordinate - individual.y_coordinate

        for line in self.layout.lines:
            assert isinstance(line, Line)
            line.y1_coordinate = max_y_coordinate - line.y1_coordinate
            line.y2_coordinate = max_y_coordinate - line.y2_coordinate
            line.y1_coordinate += self.layout.positions[0][0].size
            line.y2_coordinate += self.layout.positions[0][0].size
