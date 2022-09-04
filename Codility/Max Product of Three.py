"""
# MaxProductOfThree
Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R)
https://codility.com/programmers/task/max_product_of_three/
## Problem Description
A non-empty array A consisting of N integers is given.
The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:
        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.
Write a function:
    def solution(A)
that, given a non-empty array A, returns the value of the maximal product of any triplet.
For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.
Write an efficient algorithm for the following assumptions:
        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
----------------
## Notes
Sorting the array then multiplying the three biggest numbers will only get you a score of 44%.
The 'trick' is that two negatives make a positive.
eg: [-100, -100, -100, 0, 50, 50, 50]
The product of the top 3 is 125000,
but the product of the bottom two (-100, 100) with the top one (50) is 500000!
## Solution O(N*log(N))
1. Sort them
2. Return the larger product of
    * the lowest 2 numbers and the highest number, or
    * the highest 3 numbers
https://app.codility.com/demo/results/training4Z42TU-R8E/
"""

def solution(A):
    """
    :param A: list[int]
    :return: [int]
    """
    A.sort()
    return max(
        A[0] * A[1] * A[-1],
        A[-3] * A[-2] * A[-1]
    )
