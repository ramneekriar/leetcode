# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

# Write a function:

# def solution(A, K)

# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

def solution(A, K):
    # write your code in Python 3.6
    if A:
        num = K % len(A)
        if num == 0:
            return A
        else:
            return A[len(A) - num:] + A[:len(A) - num]
    return A