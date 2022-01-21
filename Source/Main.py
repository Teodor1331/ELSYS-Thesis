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
        assert isinstance(pedigree, PedigreeFamily)

        graph = Graph(pedigree)
        print(graph.vertices_individuals)
        print(graph.vertices_mating_units)
        print(graph.vertices_sibship_units)
        print()

        print(graph.graph_instance.edges())
        print(graph.graph_instance.nodes())
        print(len(graph.graph_instance.edges()))


        print("Edges from rule A (-): ", graph.find_edges_rule_a(), '\n')
        print("Edges from rule B (-): ", graph.find_edges_rule_b()[0], '\n')
        print("Edges from rule B (+): ", graph.find_edges_rule_b()[1], '\n')
        print("Edges from rule C (-): ", graph.find_edges_rule_c()[0], '\n')
        print("Edges from rule C (+): ", graph.find_edges_rule_c()[1], '\n')
        print("Edges from rule D (+): ", graph.find_edges_rule_d(), '\n')
        print("Edges from rule E (-): ", graph.find_edges_rule_e(), '\n')

        print("Validation of rules:", graph.validate_edges_by_rules())


if __name__ == '__main__':
    main()
