from Loader     import Loader
from Builder    import Builder
from Graph      import Graph

from FamilyUnits    import Individual
from PedigreeFamily import PedigreeFamily


import sys


def main():
    loader = Loader(sys.argv[1])
    builder = Builder(loader.file_data)
    
    for pedigree in builder.file_pedigrees:
        graph = Graph(pedigree)
        print(graph.vertices_individuals)
        print(graph.vertices_mating_units)
        print(graph.vertices_sibship_units)
        print()

        print(graph.graph_instance.edges())
        print(graph.graph_instance.nodes())


if __name__ == '__main__':
    main()
