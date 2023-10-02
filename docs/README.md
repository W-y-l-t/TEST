# **Geometric Lib**

## **Circle** - contains functions for working with a circle 

### *Functions*

> `def area(r)` Takes the variable **r** and returns the area of the circle.
> `def perimeter(r)` Takes the variable **r** and returns the perimeter of the circle.

### *Examples*
```python
import math
    
def area(r):
    return math.pi * r * r
    
def perimeter(r):
    return 2 * math.pi * r

a = area(10) # a = 314,159265
p = perimeter(10) #p = 62,831853
```

## **Square** - contains functions for working with a square

### *Functions*

> `def area` Takes the variable **a** and returns the area of the square.
> `def perimeter` Takes the variable **a** and returns the perimeter of the square.

### *Examples*
```python
def area(a):
    return a * a
    
def perimeter(a):
    return 4 * a

a = area(5) # a = 25
p = perimeter(7) # p = 28
```

## **Triangle** - contains functions for working with a triangle

### *Functions*

> `def area` Takes the variables **a** and **h** and returns the area of the triangle.
> `def perimeter`Takes three sides of a triangle **a**, **b**, **c** and returns the perimeter of the triangle.

### *Examples*
```python
def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c
    
a = area(8, 2) # a = 8
p = perimeter(1, 13, 7) # p = 21
```
## **Rectangle** - contains functions for working with a rectangle

### *Functions*

> `def area` Takes the variables **a** and **b** and returns the area of the rectangle.
> `def perimeter` Takes the variables **a** and **b** and returns the perimeter of the rectangle.

### *Examples*
```python
def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b) * 2
    
a = area(10, 10) # a = 100
p = perimeter(7, 2) # p = 18
```
# **Commits**

1. 8ba9aeb3cea847b63a91ac378a2a6db758682460
> `L-03: Circle and square added`

2. d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD) 
> `L-03: Docs added`

3. 9f777a56022bc682670115c1f2fdfe21de1d74f1 
> `[Feat] Added triangle.py`

4. 2732fc8ea42cd0c2ddb5dcaf6645e679082eec2d 
> `[Feat] Added rectangle.py`

5. a0ae412e285b88c5ac79623d20f8650804b48e6a (main) 
> `[Fix] Fixed rectangle perimetr bug`

6. f846cf8f0845268c5d3c32a460335600a743e8f8 (HEAD -> new_features_409537) 
> `[Feat] Add documentation and comments to the project`

7. ef14722cc0dec60c056aeb86713e2960bcc1d9f3 (HEAD -> main) 
> `[Feat] Add comments to the README.md`
