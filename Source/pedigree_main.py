# This Python files uses the following encoding: UTF-8

"""The module manages the logic of creating a pedigree visualization."""

import os
import sys
import shutil
import argparse

import matplotlib.pyplot as plt

from logic.pedigree_builder import Loader
from logic.pedigree_builder import Builder

from logic.pedigree_family import PedigreeFamily

from logic.pedigree_graph import Graph
from logic.pedigree_graph import SandwichInstance
from logic.pedigree_graph import ProblemSolver

from logic.pedigree_layouter import Layout
from logic.pedigree_drawer import LayoutDrawer
from logic.pedigree_drawer import PDFBuilder
from logic.pedigree_drawer import validate_colors_statuses


def main() -> None:
    """Manage the consequence in the logic of pedigree vizualization."""
    parser = argparse.ArgumentParser(description='Manage a Pedigree File.')
    parser.add_argument('-o', dest='file_name')
    parser.add_argument('-clean', action='store_true', dest='clean_flag')
    arguments = parser.parse_args()

    if arguments.file_name:
        loader = Loader(arguments.file_name)
        builder = Builder(loader.file_data)

        colors = {'affected': input('Input the color for the affected individuals: '),
                  'unaffected': input('Input the color for the unaffected individuals: '),
                  'unknown': input('Input the colors for the unknown individuals: ')}

        if len(set(colors.values())) != 3:
            print('The colors for the statuses should be different!')
            sys.exit(1)

        if 'black' in colors.values():
            print('The color for the statuses cannot be black!')
            sys.exit(2)

        if not validate_colors_statuses(colors):
            print('Some of the colors are unknown!')
            sys.exit(3)

        if not os.path.isdir('./Visualizations'):
            os.mkdir('./Visualizations')

        for pedigree in builder.file_pedigrees:
            assert isinstance(pedigree, PedigreeFamily)

            graph = Graph(pedigree)

            sandwich = SandwichInstance(
                graph.vertices_pedigree_union,
                graph.mandatory_graph,
                graph.forbidden_graph
            )

            solver = ProblemSolver(sandwich)

            if solver.solved_intervals is None:
                message = 'There is not an interval realization for the pedigree {}!'
                raise Exception(message.format(pedigree.pedigree_identifier))

            if solver.solved_intervals is not None:
                layouter = Layout(solver.solved_intervals)
                layout_drawer = LayoutDrawer(layouter, 0, 0, colors)
                figure = layout_drawer.draw(pedigree.pedigree_identifier)
                file_name = './Visualizations/' + pedigree.pedigree_identifier + '.pdf'

                with PDFBuilder(file_name) as pdf_drawer:
                    pdf_drawer.savefig(figure)
                    plt.close(figure)
                    print('A visualization of the pedigree was created!')      

    if arguments.clean_flag:
        if not os.path.isdir('./Visualizations'):
            print('There is no folder for the visualiations!')
        else:
            shutil.rmtree('./Visualizations')
            print('All pedigree visualizations were deleted!')


if __name__ == '__main__':
    main()
