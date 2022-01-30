"""
Math constants and functions for precise calculations.
"""

import math
import decimal

# Set the decimal precision to 100 digits.
decimal.getcontext().prec = 100


def pi() -> decimal.Decimal:
    """
    Evaluate the decimal value for pi
    using the Taylor series for the arcsine function.
    """

    _pi = decimal.Decimal(0)

    # The first 200 nonzero terms of the Taylor series.
    for i in range(200):
        term = decimal.Decimal(1)

        term *= math.factorial(2 * i)
        term *= decimal.Decimal(1 / 2) ** (2 * i + 1)
        term /= 4 ** i
        term /= math.factorial(i) ** 2
        term /= 2 * i + 1

        _pi += 6 * term

    return _pi


def sin(x: decimal.Decimal) -> decimal.Decimal:
    """
    Evaluate the sine of an angle (in radians)
    using the Taylor series for the sine function.
    """

    assert isinstance(x, decimal.Decimal)

    _sin = decimal.Decimal(0)

    # The first 50 nonzero terms of the Taylor series.
    for i in range(50):
        term = decimal.Decimal(1)

        term *= (-1) ** i
        term *= x ** (2 * i + 1)
        term /= math.factorial(2 * i + 1)

        _sin += term

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
        term = decimal.Decimal(1)

        term *= (-1) ** i
        term *= x ** (2 * i)
        term /= math.factorial(2 * i)

        _cos += term

    return _cos
