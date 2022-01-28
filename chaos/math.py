"""
Math constants and functions for precise calculations.
"""

import math
import decimal

# Set the decimal precision to 100 digits.
decimal.getcontext().prec = 100


def sin(x: decimal.Decimal) -> decimal.Decimal:
    """
    Evaluate the sine of an angle (in radians)
    using the Taylor series for the sine function.
    """

    assert isinstance(x, decimal.Decimal)

    _sin = decimal.Decimal(0)

    # The first 50 nonzero terms of the Taylor series.
    for i in range(50):
        term = 2 * i + 1

        _sin += (-1) ** i * x ** term / math.factorial(term)

    return _sin


def cos(x: decimal.Decimal) -> decimal.Decimal:
    """
    Evaluate the cosine of an angle (in radians)
    using the Taylor series for the cosine function.
    """

    assert isinstance(x, decimal.Decimal)

    _cos = decimal.Decimal(0)

    # The first 50 nonzero terms of the Taylor series.
    for i in range(50):
        term = 2 * i

        _cos += (-1) ** i * x ** term / math.factorial(term)

    return _cos
