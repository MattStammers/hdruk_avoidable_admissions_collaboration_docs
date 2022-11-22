"""Provide a method for calculating thrombosis

This module allows the user to make the calculations required to detect thrombosis

Examples:
    >>> from thrombocalc import thrombocalc
    >>> thrombocalc.calc(200, 4000, 2)

"""

def thrombocalc(plts, ddimer, events) -> float:
    """Compute and return the results
    ...
    """
    return float(plts * ddimer * events)

