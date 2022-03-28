# This Python file uses the following encoding: UTF-8

"""Test module on the enumerations of the Individual properties."""

import inspect

from logic.pedigree_fields import Sex
from logic.pedigree_fields import Status
from logic.pedigree_fields import Role


def test_imported_modules():
    """Test Module Inner Imports."""
    assert inspect.ismodule(inspect)


def test_sex_enumeration_instances():
    """Test Sex Enumeration Type Instances."""
    assert isinstance(Sex.UNKNOWN, Sex)
    assert isinstance(Sex.MALE, Sex)
    assert isinstance(Sex.FEMALE, Sex)
    assert inspect.isclass(Sex)


def test_sex_enumeration_members():
    """Test Sex Enumeration Type Members."""
    assert 'UNKNOWN' in Sex.__members__
    assert 'MALE' in Sex.__members__
    assert 'FEMALE' in Sex.__members__


def test_sex_enumeration_names():
    """Test Sex Enumeration Type Names."""
    assert Sex.UNKNOWN.name == 'UNKNOWN'
    assert Sex.MALE.name == 'MALE'
    assert Sex.FEMALE.name == 'FEMALE'


def test_sex_enumeration_values():
    """Test Sex Enumeration Type Values."""
    assert Sex.UNKNOWN.value == 0
    assert Sex.MALE.value == 1
    assert Sex.FEMALE.value == 2


def test_status_enumeration_instances():
    """Test Status Enumeration Type."""
    assert isinstance(Status.UNKNOWN, Status)
    assert isinstance(Status.UNAFFECTED, Status)
    assert isinstance(Status.AFFECTED, Status)
    assert inspect.isclass(Status)


def test_status_enumeration_members():
    """Test Status Enumeration Members."""
    assert 'UNKNOWN' in Status.__members__
    assert 'UNAFFECTED' in Status.__members__
    assert 'AFFECTED' in Status.__members__


def test_status_enumeration_names():
    """Test Status Enumeration Names."""
    assert Status.UNKNOWN.name == 'UNKNOWN'
    assert Status.UNAFFECTED.name == 'UNAFFECTED'
    assert Status.AFFECTED.name == 'AFFECTED'


def test_status_enumeration_values():
    """Test Status Enumeration Values."""
    assert Status.UNKNOWN.value == 0
    assert Status.UNAFFECTED.value == 1
    assert Status.AFFECTED.value == 2


def test_role_enumeration_instances():
    """Test Role Enumeration Type."""
    assert isinstance(Role.UNKNOWN, Role)
    assert isinstance(Role.PROBAND, Role)
    assert isinstance(Role.FATHER, Role)
    assert isinstance(Role.MOTHER, Role)
    assert isinstance(Role.BROTHER, Role)
    assert isinstance(Role.SISTER, Role)
    assert isinstance(Role.GRANDFATHER, Role)
    assert isinstance(Role.GRANDMOTHER, Role)
    assert inspect.isclass(Role)


def test_role_enumeration_members():
    """Test Role Enumeration Members."""
    assert 'UNKNOWN' in Role.__members__
    assert 'PROBAND' in Role.__members__
    assert 'FATHER' in Role.__members__
    assert 'MOTHER' in Role.__members__
    assert 'BROTHER' in Role.__members__
    assert 'SISTER' in Role.__members__
    assert 'GRANDFATHER' in Role.__members__
    assert 'GRANDMOTHER' in Role.__members__


def test_role_enumeration_names():
    """Test Role Enumeration Names."""
    assert Role.UNKNOWN.name == 'UNKNOWN'
    assert Role.PROBAND.name == 'PROBAND'
    assert Role.FATHER.name == 'FATHER'
    assert Role.MOTHER.name == 'MOTHER'
    assert Role.BROTHER.name == 'BROTHER'
    assert Role.SISTER.name == 'SISTER'
    assert Role.GRANDFATHER.name == 'GRANDFATHER'
    assert Role.GRANDMOTHER.name == 'GRANDMOTHER'


def test_role_enumeration_values():
    """Test Role Enumeration Values."""
    assert Role.UNKNOWN.value == 0
    assert Role.PROBAND.value == 1
    assert Role.FATHER.value == 2
    assert Role.MOTHER.value == 3
    assert Role.BROTHER.value == 4
    assert Role.SISTER.value == 5
    assert Role.GRANDFATHER.value == 6
    assert Role.GRANDMOTHER.value == 7
