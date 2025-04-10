import pytest
from pn_sequence import is_first_postulate_true, is_second_postulate_true, is_third_postulate_true, is_pn_sequence

SEQUENCE = "011001000111100111"
PN_SEQUENCES = [
    "0001011",
    "0011101",
    "011001000111101",
    "111100010011010",
    "000100110101111",
    "0000100101100111110001101110101"
]

def test_first_postulate():
    """When given a pn-sequence, the test for the first postulate should return True."""
    for seq in PN_SEQUENCES:
        assert is_first_postulate_true(seq)


def test_first_postulate_err_sequence():
    """When given a non-pn-sequence, the test for the first postulate should return False."""
    assert not is_first_postulate_true(SEQUENCE)


def test_second_postulate():
    """When given a pn-sequence, the test for the second postulate should return True."""
    for seq in PN_SEQUENCES:
        assert is_second_postulate_true(seq)


def test_second_postulate_err_sequence():
    """When given a non-pn-sequence, the test for the second postulate should return False."""
    assert not is_second_postulate_true(SEQUENCE)


def test_third_postulate():
    """When given a pn-sequence, the test for the third postulate should return True."""
    for seq in PN_SEQUENCES:
        assert is_third_postulate_true(seq)


def test_third_postulate_err_sequence():
    """When given a non-pn-sequence, the test for the third postulate should return False."""
    assert not is_third_postulate_true(SEQUENCE)


def test_pn():
    """When given a pn-sequence, the tests for all postulates should return True."""
    for seq in PN_SEQUENCES:
        assert is_pn_sequence(seq)


def test_pn_err_sequence():
    """When given a non pn-sequence, the tests for all postulates should return False."""
    assert not is_pn_sequence(SEQUENCE)

def test_not_binary_sequence():
    """When given a non-binary sequence, should raise ValueError."""
    with pytest.raises(ValueError):
        is_pn_sequence("1234")