#!/usr/bin/env python3

"add_arrays = __import__('4-line_up')"


def add_arrays(arr1, arr2):
    """Add two arrays element-wise."""
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
