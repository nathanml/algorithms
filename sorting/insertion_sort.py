"""
Insertion Sort implementation where A is the array to be sorted
"""


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j >= 1 and A[j] < A[j - 1]:
            tmp = A[j]
            A[j] = A[j - 1]
            A[j - 1] = tmp
    return A


test_array_1 = [10, 2, 8, 3, 19, 21, 11, 8, 15]
print("Test Array 1 : ", test_array_1)
print("Sorted Array 1: ", insertion_sort(test_array_1))

test_array_2 = [1, 2, 8, 3, 5, 4, 11, 9, 15]
print("Test Array 2 : ", test_array_2)
print("Sorted Array 2: ", insertion_sort(test_array_2))
