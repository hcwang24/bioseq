def transcribe(seq):
    """Transcribe the DNA sequence to RNA

    Args:
        seq (string): Input DNA sequence

    Returns:
        string: Transcribed RNA sequence
    """
    ts_seq = []
    for nuc in seq:
        if nuc == "C":
            ts_seq.append("G")
        elif nuc == "G":
            ts_seq.append("C")
        elif nuc == "A":
            ts_seq.append("U")
        elif nuc == "T":
            ts_seq.append("A")
    return "".join(ts_seq)
