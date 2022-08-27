from types import GeneratorType
import math


"""
This Module contains different series that converge to Pi
Each function is a Generator that yield terms that go closer and closer to Pi
"""


def series1(end: int|None = int(1e100), /) -> GeneratorType:
    """π = ∑ 4 * (-1)ⁿ⁺¹ / (2n-1)
    ::param: end: represents the total number of terms in the summation"""

    total = 0
    for n in range(1, end+1):
        yield (total := (total + (4 * pow(-1, n+1) / (2*n - 1))))


def series2(end: int|None = int(1e100), /) -> GeneratorType:
    """π = 3 + ∑ (-1)ⁿ⁺¹ / (n*(2n+1)*(n+1))
    ::param: end: represents the total number of terms in the summation"""

    total = 3
    for n in range(1, end+1):
        yield (total := (total + (pow(-1, n+1) / (n * (2*n+1) * (n+1)))))


def series3(end: int|None = int(1e100), /) -> GeneratorType:
    """π = ∑ √(12) * (-3)¹⁻ⁿ / (2n-1)
    ::param: end: represents the total number of terms in the summation"""

    total = 0
    for n in range(1, end+1):
        yield (total := (total + (math.sqrt(12) * pow(-3, 1-n) / (2*n - 1))))