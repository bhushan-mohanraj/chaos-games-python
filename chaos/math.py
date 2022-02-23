"""
Math constants and functions for precise calculations.
"""

import math
import decimal
from decimal import Decimal as D

# Set the decimal precision to 100 digits.
decimal.getcontext().prec = 100


def get_pi() -> D:
    """
    Evaluate the decimal value for pi
    using the Taylor series for the arcsine function.
    """

    pi = D(0)

    # The first 200 nonzero terms of the Taylor series.
    for i in range(200):
        term = D(1)

        term *= math.factorial(2 * i)
        term *= D(1 / 2) ** (2 * i + 1)
        term /= 4**i
        term /= math.factorial(i) ** 2
        term /= 2 * i + 1

        pi += 6 * term

    return pi


# A constant containing the value of pi.
PI = get_pi()


def get_sin(x: D) -> D:
    """
    Evaluate the sine of an angle (in radians)
    using the Taylor series for the sine function.
    """

    assert isinstance(x, D)

    sin = D(0)

    # The first 50 nonzero terms of the Taylor series.
    for i in range(50):
        term = D(1)

        term *= (-1) ** i
        term *= x ** (2 * i + 1)
        term /= math.factorial(2 * i + 1)

        sin += term

    return sin


def get_cos(x: D) -> D:
    """
    Evaluate the cosine of an angle (in radians)
    using the Taylor series for the cosine function.
    """

    assert isinstance(x, D)

    cos = D(0)

    # The first 50 nonzero terms of the Taylor series.
    for i in range(50):
        term = D(1)

        term *= (-1) ** i
        term *= x ** (2 * i) if i > 0 else 1
        term /= math.factorial(2 * i)

        cos += term

    return cos
