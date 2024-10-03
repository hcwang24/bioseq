from bioseq import gc_count
import pytest

def test_standard_case():
    """Testing the standard input cases"""
    assert gc_count("ATGC") == 0.50, "Incorrect GC calculation."
    assert gc_count("ATGCATGC") == 0.50, "Incorrect GC calculation."
    assert gc_count("AAAAAAAAA") == 0, "Incorrect GC calculation."
    assert gc_count("GGGGCCCC") == 1, "Incorrect GC calculation."
    
def test_exceptions():
    """Testing cases where it throws an exception."""
    with pytest.raises(Exception):
        assert gc_count("")