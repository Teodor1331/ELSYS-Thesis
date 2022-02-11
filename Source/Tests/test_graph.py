import sys
import pytest
import networkx
import ordered_set

sys.path.append('..')

from loader import Loader
from builder import Builder
from family_units import Individual
from family_units import MatingUnit
from family_units import SibshipUnit
from pedigree_family import PedigreeFamily
from graph import Graph


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
        Graph(None)
        Graph(bool)
        Graph(int)
        Graph(float)
        Graph(complex)
        Graph(str)


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

    assert graph1.vertices_individuals[0] == Individual(['ped', 'father', '0', '0', '1', '2', 'prb'])
    assert graph1.vertices_individuals[1] == Individual(['ped', 'mother', '0', '0', '2', '1', 'prb'])
