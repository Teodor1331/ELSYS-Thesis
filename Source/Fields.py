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
    PROBAND     =   1
