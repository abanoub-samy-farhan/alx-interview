#!/usr/bin/python3
def pascal_triangle(n):
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        pre = []
        for j in range(i + 1):
            if j == 0 or j == i:
                pre.append(1)
                continue
            else:
                pre.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
        pascal.append(pre)

    return pascal