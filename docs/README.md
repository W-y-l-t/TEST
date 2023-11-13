# **Geometric Lib**

# **Methods**

## **Circle.py** - contains functions for working with a circle 

### *Functions*

> `def area(r)` Takes the variable **r** and returns the area of the circle.
> 
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

##

## **Square.py** - contains functions for working with a square

### *Functions*

> `def area` Takes the variable **a** and returns the area of the square.
> 
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

##

## **Triangle.py** - contains functions for working with a triangle

### *Functions*

> `def area` Takes the variables **a** and **h** and returns the area of the triangle.
> 
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

##

## **Rectangle.py** - contains functions for working with a rectangle

### *Functions*

> `def area` Takes the variables **a** and **b** and returns the area of the rectangle.
> 
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

##

# **Commits**

| Hash          | Commit name                                          |
|---------------|------------------------------------------------------|
| ***8ba9aeb*** | L-03: Circle and square added                        |
| ***d078c8d*** | L-03: Docs added                                     |
| ***9f777a5*** | [Feat] Added triangle.py                             |
| ***2732fc8*** | [Feat] Added rectangle.py                            |
| ***a0ae412*** | [Fix] Fixed rectangle perimetr bug                   |
| ***f846cf8*** | [Feat] Add documentation and comments to the project |
| ***dae87d5*** | [Feat] Add all commits to the documentation          |
| ***ef14722*** | [Feat] Add comments to the README.md                 |
| ***64bacdd*** | Add last commit to the documentation                 |
| ***cd0b316*** | [Feat] Update README.md                              |
| ***0c4d920*** | Update README.md                                     | 
| ***817179d*** | Update README.md                                     |
| ***8a092aa*** | Update README.md                                     |
| ***399f6b1*** | Merge "Lab 2" branch to main                         |
| ***35cc012*** | [Feat] Added unit tests for all files                |
| ***0cd9d78*** | File circle.py moved to the methods folder           |
| ***29989df*** | File rectangle.py moved to the methods folder        |
| ***952252b*** | File square.py moved to the methods folder           | 
| ***8467e48*** | File triangle.py moved to the methods folder         | 