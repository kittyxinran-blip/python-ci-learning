"""Small conversion-rate calculation used to practise automated testing."""


def conversion_rate(visitors, purchases):
    """Return a percentage; reject invalid counts and handle zero traffic."""
    if type(visitors) is not int or type(purchases) is not int:
        raise TypeError("Counts must be integers")
    if visitors < 0 or purchases < 0 or purchases > visitors:
        raise ValueError("Require 0 <= purchases <= visitors")
    if visitors == 0:
        return 0.0
    return round(purchases / visitors * 100, 2)
