import sys, pytest
sys.path.append('..')

from Fields import Sex, Status, Role


def test_sex_enumeration():
    assert 'UNKNOWN' in Sex._member_names_
    assert 'MALE' in Sex._member_names_
    assert 'FEMALE' in Sex._member_names_

    assert 0 in Sex._value2member_map_
    assert 1 in Sex._value2member_map_
    assert 2 in Sex._value2member_map_

    assert isinstance(Sex.UNKNOWN, Sex)
    assert isinstance(Sex.MALE, Sex)
    assert isinstance(Sex.FEMALE, Sex)


def test_status_enumeration():
    assert 'UNKNOWN' in Status._member_names_
    assert 'AFFECTED' in Status._member_names_
    assert 'UNAFFECTED' in Status._member_names_

    assert 0 in Status._value2member_map_
    assert 1 in Status._value2member_map_
    assert 2 in Status._value2member_map_

    assert isinstance(Status.UNKNOWN, Status)
    assert isinstance(Status.AFFECTED, Status)
    assert isinstance(Status.UNAFFECTED, Status)


def test_role_enumeration():
    assert 'PROBAND' in Role._member_names_
    assert 'FATHER' in Role._member_names_
    assert 'MOTHER' in Role._member_names_
    assert 'BROTHER' in Role._member_names_
    assert 'SISTER' in Role._member_names_
    assert 'GRANDFATHER' in Role._member_names_
    assert 'GRANDMOTHER' in Role._member_names_
    
    assert 0 in Role._value2member_map_
    assert 1 in Role._value2member_map_
    assert 2 in Role._value2member_map_
    assert 3 in Role._value2member_map_
    assert 4 in Role._value2member_map_
    assert 5 in Role._value2member_map_
    assert 6 in Role._value2member_map_

    assert isinstance(Role.PROBAND, Role)
    assert isinstance(Role.FATHER, Role)
    assert isinstance(Role.MOTHER, Role)
    assert isinstance(Role.BROTHER, Role)
    assert isinstance(Role.SISTER, Role)
    assert isinstance(Role.GRANDFATHER, Role)
    assert isinstance(Role.GRANDMOTHER, Role)
