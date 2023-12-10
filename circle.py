import math


def area(r):
    """
    Returns the area of the circle by the specified radius parameter.

        Parameters:
                r (float / int): circle radius

        Return value:
                area (float): the area of a circle of radius r

    """
    if not isinstance(r, int) and not isinstance(r, float):
        return TypeError
    elif r < 0:
        return ArithmeticError
    return math.pi * r * r


def perimeter(r):
    """
    Returns the length of the circle according to the specified radius parameter.

        Parameters:
                r (float / int): circle radius

        Return value:
                perimeter (float): the circumference of radius r

    """
    if not isinstance(r, int) and not isinstance(r, float):
        return TypeError
    elif r < 0:
        return ArithmeticError
    return 2 * math.pi * r
