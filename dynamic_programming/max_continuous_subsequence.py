"""
Dynamic Programming Algorithm for calculating the maximum sum
of a contiguous subsequence within an array of integers.
"""


def maximum_contiguous_subsequence_sum(A):
    S = [0 for i in range(len(A))]
    S[len(A) - 1] = A[len(A) - 1]
    for i in reversed(range(len(A)-1)):
        S[i] = max(A[i], A[i] + S[i+1])
    return max(S)

test_array1 = [25, -11, 15, 16, -20]
print("Test Array 1 : ", test_array1)
print("Test 1 Max contiguous subsequence sum : ", maximum_contiguous_subsequence_sum(test_array1))

test_array2 = [250, -119, 150, 160, -20, -215, -32, 349, 12, -2452, 1000, 240]
print("Test Array 2 : ", test_array2)
print("Test 1 Max contiguous subsequence sum : ", maximum_contiguous_subsequence_sum(test_array2))