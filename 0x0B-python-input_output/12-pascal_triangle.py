#!/usr/bin/python3
"""Definition of a pascal's triangle function."""


def pascal_triangle(n):
    """Representation of pascal size n

    Returns a list of integers representing triangl
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
