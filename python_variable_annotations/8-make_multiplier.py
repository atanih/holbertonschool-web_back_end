#!/usr/bin/env python3
"""Module that provides a type-annotated multiplier factory."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        """Return n multiplied by the captured multiplier."""
        return n * multiplier
    return multiply
