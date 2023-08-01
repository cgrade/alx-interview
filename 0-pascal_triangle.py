#!/usr/bin/python3

"""
This Module contain algorithm to construct a pascal triangle
from the given input 'n' by a user
where 'n' is the number of rows in the pascal triangle
"""

def pascal_triangle(n):
    """A functionn that returns Pascal triangle with n rows"""

    # initializing the outer list ()
    outterList = []

    # iterating over the range of 'n'
    for eachRow in range(n):
        # initializing the inner list that rep. the columns
        innerList = []

        # iterating
        for eachCol in range(eachRow + 1):
            if eachCol == 0 or eachCol == eachRow:
                innerList.append(1)
            else:
                innerList.append(outterList[eachRow -1][eachCol - 1] + outterList[eachRow - 1][eachCol])
        outterList.append(innerList)
    return(outterList)

