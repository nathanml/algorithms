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

