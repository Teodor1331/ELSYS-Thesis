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

    assert Sex.UNKNOWN.value == 0
    assert Sex.MALE.value == 1
    assert Sex.FEMALE.value == 2


def test_status_enumeration():
    assert 'UNKNOWN' in Status._member_names_
    assert 'UNAFFECTED' in Status._member_names_
    assert 'AFFECTED' in Status._member_names_

    assert 0 in Status._value2member_map_
    assert 1 in Status._value2member_map_
    assert 2 in Status._value2member_map_

    assert isinstance(Status.UNKNOWN, Status)
    assert isinstance(Status.UNAFFECTED, Status)
    assert isinstance(Status.AFFECTED, Status)

    assert Status.UNKNOWN.value == 0
    assert Status.UNAFFECTED.value == 1
    assert Status.AFFECTED.value == 2


def test_role_enumeration():
    assert 'UNKNOWN' in Role._member_names_
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
    assert 7 in Role._value2member_map_

    assert isinstance(Role.UNKNOWN, Role)
    assert isinstance(Role.PROBAND, Role)
    assert isinstance(Role.FATHER, Role)
    assert isinstance(Role.MOTHER, Role)
    assert isinstance(Role.BROTHER, Role)
    assert isinstance(Role.SISTER, Role)
    assert isinstance(Role.GRANDFATHER, Role)
    assert isinstance(Role.GRANDMOTHER, Role)

    assert Role.UNKNOWN.value == 0
    assert Role.PROBAND.value == 1
    assert Role.FATHER.value == 2
    assert Role.MOTHER.value == 3
    assert Role.BROTHER.value == 4
    assert Role.SISTER.value == 5
    assert Role.GRANDFATHER.value == 6
    assert Role.GRANDMOTHER.value == 7
