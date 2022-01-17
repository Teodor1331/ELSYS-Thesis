import sys
import pytest


sys.path.append('..')


from Loader import Loader


def test_loader_instance():
    loader1 = Loader('../../Examples/TXT Examples/Pedigree1.txt')
    loader2 = Loader('../../Examples/TXT Examples/Pedigree2.txt')

    assert isinstance(loader1, Loader)
    assert isinstance(loader2, Loader)
