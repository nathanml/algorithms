"""
Merge Sort implementation where A is the array to be sorted
"""

'''
Helper function for merging 2 sorted sub-lists into one sorted list A.
'''


def merge(A, l1, l2):
    for i in range(len(A)):
        # If L1 empty, add top of L2
        if (len(l1)) == 0:
            A[i] = l2[0]
            l2.pop(0)
        # If L2 empty, add top of L1
        elif (len(l2)) == 0:
            A[i] = l1[0]
            l1.pop(0)
        # Else add smaller of 2 lists
        elif l1[0] < l2[0]:
            A[i] = l1[0]
            l1.pop(0)
        else:
            A[i] = l2[0]
            l2.pop(0)
    return A


'''
Merge Sort Algorithm
'''


def merge_sort(A):
    sorted_list_1, sorted_list_2 = A[:len(A) // 2], A[len(A) // 2:]
    # If first half of list is unsorted, sort
    if len(A) // 2 > 1:
        sorted_list_1 = merge_sort(sorted_list_1)
    # If second half of list is unsorted, sort
    if len(A) // 2 + 1 < len(A):
        sorted_list_2 = merge_sort(sorted_list_2)
    # Once both sublists are sorted, merge
    return merge(A, sorted_list_1, sorted_list_2)


test_array_1 = [10, 2, 8, 3, 19, 21, 11, 8, 15]
print("Test Array 1 : ", test_array_1)
print("Sorted Array 1: ", merge_sort(test_array_1))

test_array_2 = [1, 2, 8, 3, 5, 4, 11, 9, 15]
print("Test Array 2 : ", test_array_2)
print("Sorted Array 2: ", merge_sort(test_array_2))
