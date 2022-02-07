from enum import Enum


class Sex(Enum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2


class Status(Enum):
    UNKNOWN = 0
    UNAFFECTED = 1
    AFFECTED = 2


class Role(Enum):
    UNKNOWN = 0
    PROBAND = 1
    FATHER = 2
    MOTHER = 3
    BROTHER = 4
    SISTER = 5
    GRANDFATHER = 6
    GRANDMOTHER = 7
