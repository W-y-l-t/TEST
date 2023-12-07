def area(a):
    """
    Returns the area of the square according to the specified parameter of the side.

        Parameters:
                a (float / int): the length of the side of the square

        Return value:
                area (float / int): the area of a square with side a

    """
    if not isinstance(a, int) and not isinstance(a, float):
        return TypeError
    elif a < 0:
        return ArithmeticError
    return a * a


def perimeter(a):
    """
    Returns the perimeter of the square according to the specified parameter of the side.

        Parameters:
                a (float / int): the length of the side of the square

        Return value:
                perimeter (float / int): the perimeter of the square with side a

    """
    if not isinstance(a, int) and not isinstance(a, float):
        return TypeError
    elif a < 0:
        return ArithmeticError
    return 4 * a
