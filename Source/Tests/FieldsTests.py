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


def test_status_enumeration():
    assert 'UNKNOWN' in Status._member_names_
    assert 'AFFECTED' in Status._member_names_
    assert 'UNAFFECTED' in Status._member_names_

    assert 0 in Status._value2member_map_
    assert 1 in Status._value2member_map_
    assert 2 in Status._value2member_map_


def test_role_enumeration():
    assert 'PROBAND' in Role._member_names_
    
    assert 0 in Role._value2member_map_
