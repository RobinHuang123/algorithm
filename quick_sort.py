#!/usr/bin/env python

"""
QUICKSORT(A, p, r)
1   if p < r
2       q = PARTITION(A, p, r)
3       QUICKSORT(A, p, q-1)
3       QUICKSORT(A, q+1, r)

PATTITION(A, p, r)
1   x = A[r]
2   i = p-1
3   for j = p to r-1
4       if A[j] <= x
5           i = i + 1
6           exchange A[i] with A[j]
7   exchange A[i+1] with A[j]
8   return i + 1
"""


def quicksort(A, p=None, r=None):
    p = 0 if p is None else p
    r = len(A) - 1  if r is None else r
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


if __name__ == '__main__':
    a = [2, 5, 7, 3, 8, 9, 1, 0, 4, 6]
    quicksort(a)
    assert a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a)
