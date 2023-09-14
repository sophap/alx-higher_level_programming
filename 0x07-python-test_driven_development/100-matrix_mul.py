#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    lst1 = len(m_a)
    if lst1 == 0:
        raise ValueError("m_a can't be empty")
    lst2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if lst2 is None:
            lst2 = len(i)
            if lst2 == 0:
                raise ValueError("m_a can't be empty")
        if lst2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    lst3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if lst3 is None:
            lst3 = len(i)
            if lst3 == 0:
                raise ValueError("m_b can't be empty")
        if lst3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if lst2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(lst1):
        lst = []
        for j in range(lst3):
            n = 0
            for k in range(lst2):
                n += m_a[i][k] * m_b[k][j]
            lst.append(n)
        matrix.append(lst)
    return matrix
