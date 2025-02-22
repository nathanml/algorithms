"""
Quick Sort implementation where A is the array to be sorted
"""
import random


def quick_sort(A: list):
    if len(A) <= 1:
        return A
    else:
        # Randomly select pivot
        i = random.randint(0, len(A)-1)
        pos = A[i]
        # Partition list based on pivot
        left = [x for x in A[1:] if x < pos]
        right = [x for x in A[1:] if x >= pos]
        # Recurse
        return quick_sort(left) + [pos] + quick_sort(right)


test_array_1 = [10, 2, 8, 3, 19, 21, 11, 8, 15]
print("Test Array 1 : ", test_array_1)
print("Sorted Array 1: ", quick_sort(test_array_1))

test_array_2 = [1, 2, 8, 3, 5, 4, 11, 9, 15]
print("Test Array 2 : ", test_array_2)
print("Sorted Array 2: ", quick_sort(test_array_2))
