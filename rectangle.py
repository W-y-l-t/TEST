def area(a, b):
    """
    Returns the area of the rectangle according to the specified parameters of the sides.

        Parameters:
                a (float / int): length of the first side of the rectangle
                b (float / int): length of the second side of the rectangle
                a, b - width and length of the rectangle

        Return value:
                area (float/ int): the area of a rectangle with sides a, b

    """
    if not isinstance(a, int) and not isinstance(a, float) or not isinstance(b, int) and not isinstance(b, float):
        return TypeError
    elif a < 0 or b < 0:
        return ArithmeticError
    return a * b


def perimeter(a, b):
    """
    Returns the perimeter of the rectangle according to the specified parameters of the sides.

        Parameters:
                a (float / int): length of the first side of the rectangle
                b (float / int): length of the second side of the rectangle

        Return value:
                perimeter (float / int): the perimeter of a rectangle with sides a, b

    """
    if not isinstance(a, int) and not isinstance(a, float) or not isinstance(b, int) and not isinstance(b, float):
        return TypeError
    elif a <= 0 or b <= 0:
        return ArithmeticError
    return (a + b) * 2
