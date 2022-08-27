import numpy as np
import random
import math


def pair(side: int) -> tuple[float, float]:
    """returns random (x, y) co-ordinate pairs"""

    return random.uniform(0, side), random.uniform(0, side)


def inside(
        pair: tuple[float, float], center: tuple[float, float], radius: int
    ) -> bool:
    """returns True if the co-ordinate pair (x, y) lies inside the circle
    with given center and radius, and False in all other cases"""

    return math.dist(center, pair) < radius


def error(pi: float) -> float:
    """returns the percentage error in calculation of pi, with the argument
    being the calculated estimate of pi"""

    return 100 * (pi-math.pi) / math.pi


def calculate(in_circle: int, total: int) -> float:
    """returns calculated estimate of pi"""

    return 4 * in_circle/total