#!/usr/bin/env python

"""
Page 109
COUNTING-SORT(A, B, k)
1   let C[0..k] be a new arrary
2   for i = 0 to k
3       C[i] = 0
4   for j = 1 to A.length
5       C[A[j]] = C[A[j]] + 1
6   //C[i] now cantains the number of elements equal to i
7   for i=0 to k-1
8       C[i+1] = C[i] + C[i+1]
9   //C[i] now cantains the number of elements less than or equal to i
10  for j= A.length downto 1
11      B[C[A[j]]] = A[j]
12      C[A[j]] = C[A[j]] - 1
"""

def countingSort(A, B, k):
    C = [0] * (k + 1)
    for j in range(len(A)):
        print("C[A[j]]", j, A[j])
        C[A[j]] = C[A[j]] + 1

    for i in range(k):
        C[i+1] = C[i] + C[i+1]

    for j in range(len(A)):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1


def countingSort1(A, B, k):
    C = [0] * (k + 1)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1

    j = 0
    for i in range(k+1):
        for m in range(C[i]):
            B[j] = i
            j = j + 1


if __name__ == '__main__':
    a = [2, 5, 2, 7, 3, 8, 9, 1, 0, 4, 6]
    b = [None] * len(a)
    countingSort(a, b, 9)
    print(a)
    print(b)



