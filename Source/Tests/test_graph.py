import sys, pytest
sys.path.append('..')

from loader import Loader
from builder import Builder
from pedigree_family import PedigreeFamily
from graph import Graph


def test_graph_constructor():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    graphs_list1 = [Graph(pedigree) for pedigree in builder1.file_pedigrees]
    graphs_list2 = [Graph(pedigree) for pedigree in builder2.file_pedigrees]
    graphs_list3 = [Graph(pedigree) for pedigree in builder3.file_pedigrees]

    assert 'graphs_list1' in locals()
    assert 'graphs_list2' in locals()
    assert 'graphs_list3' in locals()

    assert locals()['graphs_list1'] is graphs_list1
    assert locals()['graphs_list2'] is graphs_list2
    assert locals()['graphs_list3'] is graphs_list3

    for graph in graphs_list1:
        assert isinstance(graph, Graph)

    for graph in graphs_list2:
        assert isinstance(graph, Graph)

    for graph in graphs_list3:
        assert isinstance(graph, Graph)

    with pytest.raises(AssertionError):
        Graph(None)
        Graph(bool)
        Graph(int)
        Graph(float)
        Graph(complex)
        Graph(str)
