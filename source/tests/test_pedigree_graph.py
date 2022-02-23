import sys
import pytest
import networkx
import ordered_set

sys.path.append('..')

from pedigree_builder import Loader
from pedigree_builder import Builder
from pedigree_units import Individual
from pedigree_units import MatingUnit
from pedigree_units import SibshipUnit
from pedigree_family import PedigreeFamily
from pedigree_graph import Graph


def test_graph_constructor():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    graph1 = Graph(builder1.file_pedigrees[0])
    graph2 = Graph(builder2.file_pedigrees[0])
    graph3 = Graph(builder3.file_pedigrees[0])

    assert 'graph1' in locals()
    assert 'graph2' in locals()
    assert 'graph3' in locals()

    assert locals()['graph1'] is graph1
    assert locals()['graph2'] is graph2
    assert locals()['graph3'] is graph3

    assert isinstance(graph1, Graph)
    assert isinstance(graph2, Graph)
    assert isinstance(graph3, Graph)

    with pytest.raises(AssertionError):
        Graph(None), Graph(bool)
        Graph(int), Graph(float), Graph(complex)
        Graph(bytes), Graph(bytearray), Graph(str)
        Graph(tuple), Graph(range)
        Graph(set), Graph(frozenset), Graph(dict)


def test_graph_destructor():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    graph1 = Graph(builder1.file_pedigrees[0])
    graph2 = Graph(builder2.file_pedigrees[0])
    graph3 = Graph(builder3.file_pedigrees[0])

    del graph1
    del graph2
    del graph3

    assert 'graph1' not in locals()
    assert 'graph2' not in locals()
    assert 'graph3' not in locals()


def test_graph_instances():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    graph1 = Graph(builder1.file_pedigrees[0])
    graph2 = Graph(builder2.file_pedigrees[0])
    graph3 = Graph(builder3.file_pedigrees[0])

    assert hasattr(graph1, 'pedigree_family')
    assert hasattr(graph2, 'pedigree_family')
    assert hasattr(graph3, 'pedigree_family')

    assert hasattr(graph1, 'vertices_individuals')
    assert hasattr(graph2, 'vertices_individuals')
    assert hasattr(graph3, 'vertices_individuals')

    assert hasattr(graph1, 'vertices_mating_units')
    assert hasattr(graph2, 'vertices_mating_units')
    assert hasattr(graph3, 'vertices_mating_units')

    assert hasattr(graph1, 'vertices_sibship_units')
    assert hasattr(graph2, 'vertices_sibship_units')
    assert hasattr(graph3, 'vertices_sibship_units')

    assert hasattr(graph1, 'vertices_pedigree_union')
    assert hasattr(graph2, 'vertices_pedigree_union')
    assert hasattr(graph3, 'vertices_pedigree_union')

    assert hasattr(graph1, 'graph_instance')
    assert hasattr(graph2, 'graph_instance')
    assert hasattr(graph3, 'graph_instance')

    assert hasattr(graph1, 'mandatory_graph')
    assert hasattr(graph2, 'mandatory_graph')
    assert hasattr(graph3, 'mandatory_graph')

    assert hasattr(graph1, 'forbidden_graph')
    assert hasattr(graph2, 'forbidden_graph')
    assert hasattr(graph3, 'forbidden_graph')

    assert isinstance(graph1.pedigree_family, PedigreeFamily)
    assert isinstance(graph2.pedigree_family, PedigreeFamily)
    assert isinstance(graph3.pedigree_family, PedigreeFamily)

    assert isinstance(graph1.vertices_individuals, list)
    assert isinstance(graph2.vertices_individuals, list)
    assert isinstance(graph3.vertices_individuals, list)

    assert isinstance(graph1.vertices_mating_units, list)
    assert isinstance(graph2.vertices_mating_units, list)
    assert isinstance(graph3.vertices_mating_units, list)
    
    assert isinstance(graph1.vertices_sibship_units, list)
    assert isinstance(graph2.vertices_sibship_units, list)
    assert isinstance(graph3.vertices_sibship_units, list)

    assert isinstance(graph1.vertices_pedigree_union, ordered_set.OrderedSet)
    assert isinstance(graph2.vertices_pedigree_union, ordered_set.OrderedSet)
    assert isinstance(graph3.vertices_pedigree_union, ordered_set.OrderedSet)

    assert isinstance(graph1.graph_instance, networkx.Graph)
    assert isinstance(graph2.graph_instance, networkx.Graph)
    assert isinstance(graph3.graph_instance, networkx.Graph)

    assert isinstance(graph1.mandatory_graph, ordered_set.OrderedSet)
    assert isinstance(graph2.mandatory_graph, ordered_set.OrderedSet)
    assert isinstance(graph3.mandatory_graph, ordered_set.OrderedSet)

    assert isinstance(graph1.forbidden_graph, ordered_set.OrderedSet)
    assert isinstance(graph2.forbidden_graph, ordered_set.OrderedSet)
    assert isinstance(graph3.forbidden_graph, ordered_set.OrderedSet)

    assert graph1.vertices_individuals != list()
    assert graph2.vertices_individuals != list()
    assert graph3.vertices_individuals != list()

    assert graph1.vertices_mating_units != list()
    assert graph2.vertices_mating_units != list()
    assert graph3.vertices_mating_units != list()
    
    assert graph1.vertices_sibship_units != list()
    assert graph2.vertices_sibship_units != list()
    assert graph3.vertices_sibship_units != list()

    assert graph1.vertices_pedigree_union != ordered_set.OrderedSet()
    assert graph2.vertices_pedigree_union != ordered_set.OrderedSet()
    assert graph3.vertices_pedigree_union != ordered_set.OrderedSet()

    assert graph1.mandatory_graph != ordered_set.OrderedSet()
    assert graph2.mandatory_graph != ordered_set.OrderedSet()
    assert graph3.mandatory_graph != ordered_set.OrderedSet()

    assert graph1.forbidden_graph != ordered_set.OrderedSet()
    assert graph2.forbidden_graph != ordered_set.OrderedSet()
    assert graph3.forbidden_graph != ordered_set.OrderedSet()

    assert len(graph1.vertices_individuals) == 6
    assert len(graph2.vertices_individuals) == 6
    assert len(graph3.vertices_individuals) == 6

    assert len(graph1.vertices_mating_units) == 1
    assert len(graph2.vertices_mating_units) == 1
    assert len(graph3.vertices_mating_units) == 1

    assert len(graph1.vertices_sibship_units) == 1
    assert len(graph2.vertices_sibship_units) == 1
    assert len(graph3.vertices_sibship_units) == 1

    assert len(graph1.vertices_pedigree_union) == 8
    assert len(graph2.vertices_pedigree_union) == 8
    assert len(graph3.vertices_pedigree_union) == 8

    individual1 = Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    individual2 = Individual(['ped', 'mother', '0', '0', '2', '1', 'null'])
    individual3 = Individual(['ped', 'son1', 'father', 'mother', '1', '2', 'null'])
    individual4 = Individual(['ped', 'son2', 'father', 'mother', '1', '1', 'null'])
    individual5 = Individual(['ped', 'dau1', 'father', 'mother', '2', '2', 'null'])
    individual6 = Individual(['ped', 'dau2', 'father', 'mother', '2', '1', 'null'])

    mating_unit = MatingUnit('ped', individual1, individual2)

    sibship_unit = SibshipUnit('ped')
    sibship_unit.add_sibling_individual(individual3)
    sibship_unit.add_sibling_individual(individual4)
    sibship_unit.add_sibling_individual(individual5)
    sibship_unit.add_sibling_individual(individual6)

    mating_unit.sibship_unit_relation = sibship_unit
    sibship_unit.mating_unit_relation = mating_unit

    assert graph1.vertices_individuals[0] == individual1
    assert graph1.vertices_individuals[1] == individual2
    assert graph1.vertices_individuals[2] == individual3
    assert graph1.vertices_individuals[3] == individual4
    assert graph1.vertices_individuals[4] == individual5
    assert graph1.vertices_individuals[5] == individual6

    assert graph2.vertices_individuals[0] == individual1
    assert graph2.vertices_individuals[1] == individual2
    assert graph2.vertices_individuals[2] == individual3
    assert graph2.vertices_individuals[3] == individual4
    assert graph2.vertices_individuals[4] == individual5
    assert graph2.vertices_individuals[5] == individual6

    assert graph3.vertices_individuals[0] == individual1
    assert graph3.vertices_individuals[1] == individual2
    assert graph3.vertices_individuals[2] == individual3
    assert graph3.vertices_individuals[3] == individual4
    assert graph3.vertices_individuals[4] == individual5
    assert graph3.vertices_individuals[5] == individual6

    assert graph1.vertices_mating_units[0] == mating_unit
    assert graph2.vertices_mating_units[0] == mating_unit
    assert graph3.vertices_mating_units[0] == mating_unit

    assert graph1.vertices_sibship_units[0] == sibship_unit
    assert graph2.vertices_sibship_units[0] == sibship_unit
    assert graph3.vertices_sibship_units[0] == sibship_unit

    assert graph1.vertices_pedigree_union[0] == individual1
    assert graph1.vertices_pedigree_union[1] == individual2
    assert graph1.vertices_pedigree_union[2] == individual3
    assert graph1.vertices_pedigree_union[3] == individual4
    assert graph1.vertices_pedigree_union[4] == individual5
    assert graph1.vertices_pedigree_union[5] == individual6
    assert graph1.vertices_pedigree_union[6] == mating_unit
    assert graph1.vertices_pedigree_union[7] == sibship_unit

    assert graph2.vertices_pedigree_union[0] == individual1
    assert graph2.vertices_pedigree_union[1] == individual2
    assert graph2.vertices_pedigree_union[2] == individual3
    assert graph2.vertices_pedigree_union[3] == individual4
    assert graph2.vertices_pedigree_union[4] == individual5
    assert graph2.vertices_pedigree_union[5] == individual6
    assert graph2.vertices_pedigree_union[6] == mating_unit
    assert graph2.vertices_pedigree_union[7] == sibship_unit

    assert graph3.vertices_pedigree_union[0] == individual1
    assert graph3.vertices_pedigree_union[1] == individual2
    assert graph3.vertices_pedigree_union[2] == individual3
    assert graph3.vertices_pedigree_union[3] == individual4
    assert graph3.vertices_pedigree_union[4] == individual5
    assert graph3.vertices_pedigree_union[5] == individual6
    assert graph3.vertices_pedigree_union[6] == mating_unit
    assert graph3.vertices_pedigree_union[7] == sibship_unit
