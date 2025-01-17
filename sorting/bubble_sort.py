"""
Bubble Sort implementation where A is the array to be sorted
"""


def bubble_sort(A):
    for i in reversed(range(1, len(A))):
        for j in range(i):
            if A[i] < A[j]:
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
    return A


test_array_1 = [10, 2, 8, 3, 19, 21, 11, 8, 15]
print("Test Array 1 : ", test_array_1)
print("Sorted Array 1: ", bubble_sort(test_array_1))

test_array_2 = [1, 2, 8, 3, 5, 4, 11, 9, 15]
print("Test Array 2 : ", test_array_2)
print("Sorted Array 2: ", bubble_sort(test_array_2))