#!/usr/bin/python3
'''
Python simple module
'''

def pascal_triangle(n):
    if n <= 0:
        return []

    pascals_triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = pascals_triangle[i - 1]
                row.append(prev_row[j - 1] + prev_row[j])
        pascals_triangle.append(row)
    return pascals_triangle
