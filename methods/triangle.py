def area(a, h):
    '''
    Returns the area of the triangle according to the specified parameters of its base and height.

        Parameters:
                a (float / int): the length of the triangle side
                h (float / int): the length of the triangle base

        Return value:
                area (float/ int): area of a triangle with base a and height h
                
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Returns the perimeter of the triangle according to the specified parameters of the sides.

        Parameters:
                a (float / int): length of the first side of the triangle
                b (float / int): length of the second side of the triangle
                c (float /int): the length of the third side of the triangle

        Return value:
                perimeter (float / int): the perimeter of a triangle with sides a, b, c
                
    '''
    return a + b + c 