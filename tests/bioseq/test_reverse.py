from bioseq import reverse
import pytest

def test_standard_case():
    """Testing the standard input cases"""
    assert reverse("ATGC") == "CGTA", "Incorrect sequence reversal."
    assert reverse("ATGCATGC") == "CGTACGTA", "Incorrect sequence reversal."
    assert reverse("AAAAAAAAA") == "AAAAAAAAA", "Incorrect sequence reversal."
    assert reverse("GGGGCCCC") == "CCCCGGGG", "Incorrect sequence reversal."
    
def test_exceptions():
    """Testing cases where it throws an exception."""
    with pytest.raises(Exception):
        assert reverse("")