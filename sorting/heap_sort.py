"""
Heap Sort implementation where A is the array to be sorted
"""

import heapq


def heap_sort(A: list):
    heapq.heapify(A)
    ret = []
    while A:
        ret.append(heapq.heappop(A))
    return ret


test_array_1 = [10, 2, 8, 3, 19, 21, 11, 8, 15]
print("Test Array 1 : ", test_array_1)
print("Sorted Array 1: ", heap_sort(test_array_1))

test_array_2 = [1, 2, 8, 3, 5, 4, 11, 9, 15]
print("Test Array 2 : ", test_array_2)
print("Sorted Array 2: ", heap_sort(test_array_2))
