#!/usr/bin/env python

import math


class Heap(object):

    def __init__(self, l):
        self.__heap = l[:]
        self.__heap_size = len(self.__heap)

    def __getitem__(self, i):
        return self.__heap[i]

    def __setitem__(self, i, v):
        if i < len(self):
            self.__heap[i] = v
        else:
            self.__heap.append(v)

    def __delitem__(self, i):
        if i < len(self):
            del self.__heap[i]
        else:
            raise Exception("Heap delete index out of range")

    def __len__(self):
        return len(self.__heap)

    @property
    def size(self):
        return self.__heap_size

    @size.setter
    def size(self, heap_size):
        self.__heap_size = heap_size

    def copy(self):
        obj = self.__class__(self.__heap)
        obj.size = self.size
        return obj

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * (i + 1)

    def height(self):
        n = math.log(len(self), 2)
        if int(n) == n:
            return n
        else:
            return int(n) + 1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < self.size and self[l] > self[i]:
            largest = l
        else:
            largest = i
        if r < self.size and  self[r] > self[largest]:
            largest = r
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.max_heapify(i-1)

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < self.size and self[l] < self[i]:
            min = l
        else:
            min = i
        if r < self.size and  self[r] < self[min]:
            min = r
        if min != i:
            self[i], self[min] = self[min], self[i]
            self.min_heapify(min)

    def build_min_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.min_heapify(i-1)

    def sort(self):
        heap = self.copy()
        heap.build_max_heap()
        length = len(heap)
        for i in range(length-1, 0, -1):
            heap[0], heap[i] = heap[i], heap[0]
            heap.size = heap.size -1
            heap.max_heapify(0)
        return heap

    def __str__(self):
        return "[%s]" % ', '.join([str(x) for x in self])


class PriorityQueue(Heap):

    """Priority Queue based on MAX-Heap"""

    def __init__(self, l):
        super().__init__(l)

    def maximum(self):
        self.build_max_heap()
        return self[0]

    def extract_max(self):
        self.build_max_heap()
        if self.size < 1:
            raise Exception("heap underflow")
        max = self[0]
        self[0] = self[self.size - 1]
        self.size = self.size - 1
        self.max_heapify(0)
        return max

    def increase_key(self, i, key):
        if key < self[i]:
            raise Exception("new key is smaller than current key")
        self[i] = key
        while i > 0 and self[self.parent(i)] < self[i]:
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            i = self.parent(i)

    def insert(self, key):
        self.size = self.size + 1
        self[self.size - 1] = -float('inf')
        self.increase_key(self.size - 1, key)


if __name__ == '__main__':
    heap = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
    heap.build_max_heap()
    print(heap)
    heap.build_min_heap()
    print(heap)
    print(heap.sort())
    q = PriorityQueue([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
    q.insert(100)
    print(q.extract_max())
    q.increase_key(1, 55)
    assert q.extract_max() ==  55, "failed"
    print(q.extract_max())
    print(q.extract_max())
