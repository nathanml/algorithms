"""
Counting Sort implementation where A is the array to be sorted
"""


def counting_sort(A, max, min):
    counts = [0 for i in range(max)]
    for i in range(len(A)):
        counts[A[i] - min] += 1
    ret = []
    for i in range(len(counts)):
        while counts[i] != 0:
            ret.append(min + i)
            counts[i] -= 1
    return ret


test_array_1 = [10, 2, 8, 3, 19, 21, 11, 8, 15]
print("Test Array 1 : ", test_array_1)
print("Sorted Array 1: ", counting_sort(test_array_1, max(test_array_1), min(test_array_1)))

test_array_2 = [1, 2, 8, 3, 5, 4, 11, 9, 15]
print("Test Array 2 : ", test_array_2)
print("Sorted Array 2: ", counting_sort(test_array_2, max(test_array_2), min(test_array_2)))
