[![Documentation Status](https://readthedocs.org/projects/bioseq/badge/?version=latest)](https://bioseq.readthedocs.io/en/latest/?badge=latest)

# bioseq

A tool for processing DNA sequences.

## Installation

```bash
$ pip install bioseq
```

## Usage

```python
from bioseq import gc_count, reverse, transcribe

seq_string = "ATCGAGCG"

# Counting GC ratio
gc_count(seq_string)

# Reversing this sequence
reverse(seq_string)

# Transcribe the sequence
transcribe(seq_string)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`bioseq` was created by HanChen Wang. It is licensed under the terms of the MIT license.

## Credits

`bioseq` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
