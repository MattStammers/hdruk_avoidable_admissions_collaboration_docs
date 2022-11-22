"""
Provide a method for calculating chest pain results

This module allows us to calculate the risk scores for individuals

Examples:
    >>> from chest_pain import calculator
    >>> calculator.cpcalc(3, 10, 200)
        ("high-risk")

"""

def cpcalc(trop1, trop2, trop3) -> float:
    """Compute and return the results
    ...
    """
    return float(trop1 * trop2 * trop3)

