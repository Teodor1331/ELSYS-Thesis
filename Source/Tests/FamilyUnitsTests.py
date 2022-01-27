import sys
import pytest


sys.path.append('..')


from FamilyUnits import Individual
from FamilyUnits import MatingUnit
from FamilyUnits import SibshipUnit


def test_individual_instances():
    individual1 = Individual(['ped1', 'father', '0', '0', '1', '0', 'null'])
    individual2 = Individual(['ped1', 'mother', '0', '0', '2', '0', 'null'])
    individual3 = None
    individual4 = None
    individual5 = None
    individual6 = None
