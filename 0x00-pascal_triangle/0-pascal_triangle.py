#!/usr/bin/python3
""" A script that returns Pascal triangle for n number"""


def pascal_triangle(n):
    """A functionn that returns Pascal triangle with n rows"""
    outterList = []

    for eachRow in range(n):
        # initializing the inner list that rep. the columns
        innerList = []
        for eachCol in range(eachRow + 1):
            if eachCol == 0 or eachCol == eachRow:
                innerList.append(1)
            else:
                innerList.append(
                    outterList[eachRow - 1][eachCol - 1] +
                    outterList[eachRow - 1][eachCol])
        outterList.append(innerList)
    return (outterList)
