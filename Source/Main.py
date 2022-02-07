import sys


from Loader import Loader
from Builder import Builder

from Graph              import Graph, SandwichInstance
from Graph              import SandwichSolver
from IntervalSandwich   import Interval
from Drawer             import Drawer
from Drawer             import PDFCreator

from FamilyUnits    import Individual
from PedigreeFamily import PedigreeFamily


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
        drawer = Drawer(solver.solved_intervals)
        pdf = PDFCreator(pedigree.pedigree_identifier)


if __name__ == '__main__':
    main()
