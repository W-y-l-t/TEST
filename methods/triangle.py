def area(a, h):
    """
    Returns the area of the triangle according to the specified parameters of its base and height.

        Parameters:
                a (float / int): the length of the triangle side
                h (float / int): the length of the triangle base

        Return value:
                area (float/ int): area of a triangle with base a and height h

    """
    if not isinstance(a, int) and not isinstance(a, float) or not isinstance(h, int) and not isinstance(h, float):
        return TypeError
    elif a < 0 or h < 0:
        return ArithmeticError
    return a * h / 2


def perimeter(a, b, c):
    """
    Returns the perimeter of the triangle according to the specified parameters of the sides.

        Parameters:
                a (float / int): length of the first side of the triangle
                b (float / int): length of the second side of the triangle
                c (float /int): the length of the third side of the triangle

        Return value:
                perimeter (float / int): the perimeter of a triangle with sides a, b, c

    """
    if not isinstance(a, int) and not isinstance(a, float) or not isinstance(b, int) and \
            not isinstance(b, float) or not isinstance(c, int) and not isinstance(c, float):
        return TypeError
    elif a <= 0 or b <= 0 or c <= 0:
        return ArithmeticError
    return a + b + c
