#!/usr/bin/env python3
"""Module that duck types an iterable object of sequences."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each sequence and its length."""
    return [(i, len(i)) for i in lst]
