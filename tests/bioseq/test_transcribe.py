from bioseq import transcribe
import pytest

def test_standard_case():
    """Testing the standard input cases"""
    assert transcribe("ATGC") == "UACG", "Incorrect transcription."
    assert transcribe("ATGCATGC") == "UACGUACG", "Incorrect transcription."
    assert transcribe("AAAAAAAAA") == "UUUUUUUUU", "Incorrect transcription."
    assert transcribe("GGGGCCCC") == "CCCCGGGG", "Incorrect transcription."
    
def test_exceptions():
    """Testing cases where it throws an exception."""
    with pytest.raises(Exception):
        assert transcribe("")