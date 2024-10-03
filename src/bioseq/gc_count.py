def gc_count(seq):
    """Calculate the GC content of a DNA Sequence

    Args:
        seq (string): Input DNA Sequence

    Returns:
        float: ratio of GC in the DNA Sequence
    """
    gc = seq.count("C") + seq.count("G")
    seq_len = len(seq)
    return gc / seq_len
