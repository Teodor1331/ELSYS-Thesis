from enum import Enum


class Sex(Enum):
    UNKNOWN     =   0
    MALE        =   1
    FEMALE      =   2


class Status(Enum):
    UNKNOWN     =   0
    UNAFFECTED  =   1
    AFFECTED    =   2


class Role(Enum):
    PROBAND         =   0
    FATHER          =   1
    MOTHER          =   2
    BROTHER         =   3
    SISTER          =   4
    GRANDFATHER     =   5
    GRANDMOTHER     =   6
