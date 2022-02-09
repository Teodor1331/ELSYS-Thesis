import sys


from loader import Loader
from builder import Builder

from graph import Graph, SandwichInstance
from graph import SandwichSolver
from interval_sandwich import Interval
from Drawer             import Drawer
from Drawer             import PDFCreator

from family_units import Individual
from pedigree_family import PedigreeFamily


def main(argv = sys.argv[1:]):
    loader = Loader(argv[0])
    builder = Builder(loader.file_data)
    
    for pedigree in builder.file_pedigrees:
        assert isinstance(pedigree, PedigreeFamily)

        graph = Graph(pedigree)

        sandwich = SandwichInstance(
            graph.vertices_pedigree_union,
            graph.required_graph,
            graph.forbidden_graph
        )

        solver = SandwichSolver(sandwich)
        print(solver.solved_intervals)
        drawer = Drawer(solver.solved_intervals)
        pdf = PDFCreator(pedigree.pedigree_identifier)


if __name__ == '__main__':
    main()
