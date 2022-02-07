import sys, pytest
sys.path.append('..')

from Loader import Loader
from Builder import Builder


def test_builder_instances():
    loader1 = Loader('../../Examples/TXT Examples/Pedigree1.txt')
    loader2 = Loader('../../Examples/TXT Examples/Pedigree2.txt')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree3.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    assert isinstance(builder1, Builder)
    assert isinstance(builder2, Builder)
    assert isinstance(builder3, Builder)


def test_builder_properties():
    loader1 = Loader('../../Examples/CSV Examples/Pedigree1.csv')
    loader2 = Loader('../../Examples/PED Examples/Pedigree1.ped')
    loader3 = Loader('../../Examples/TXT Examples/Pedigree1.txt')

    builder1 = Builder(loader1.file_data)
    builder2 = Builder(loader2.file_data)
    builder3 = Builder(loader3.file_data)

    assert isinstance(builder1.file_data, list)
    assert isinstance(builder2.file_data, list)
    assert isinstance(builder3.file_data, list)
