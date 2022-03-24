# This Python file uses the following encoding: UTF-8

"""Module with all enumerations for the Individual class properties."""

from enum import Enum


class Sex(Enum):
    """Sex Type Enumeration."""

    UNKNOWN = 0
    MALE = 1
    FEMALE = 2


class Status(Enum):
    """Status Type Enumeration."""

    UNKNOWN = 0
    UNAFFECTED = 1
    AFFECTED = 2


class Role(Enum):
    """Role Type Enumeration."""

    UNKNOWN = 0
    PROBAND = 1
    FATHER = 2
    MOTHER = 3
    BROTHER = 4
    SISTER = 5
    GRANDFATHER = 6
    GRANDMOTHER = 7
