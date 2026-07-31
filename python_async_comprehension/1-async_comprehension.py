#!/usr/bin/env python3
"""Module that collects random numbers using an async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers produced by async_generator."""
    return [number async for number in async_generator()]
