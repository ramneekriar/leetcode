"""
# Passing Cars
Count the number of passing cars on the road.
A non-empty array A consisting of N integers is given.
The consecutive elements of array A represent consecutive cars on a road.
Array A contains only 0s and/or 1s:
        0 represents a car traveling east,
        1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q),
where 0 ≤ P < Q < N, is passing when P is traveling to the east
and Q is traveling to the west.
For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
Write a function:
    def solution(A)
that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
The function should return -1 if the number of pairs of passing cars exceeds 1,000,000,000.
For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.
Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.
Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""

MAX_PAIRS = int(1e9)


def solution(A):
    """Count the number of passing cars on the road.
    :param A: list[int] A sequence of cars traveling east (0) or west (1).
    :return: [int] A count of the pairs of cars passing, or -1.
    NB: A car travelling east only 'passes' the cars travelling west, which are
    after it in the series.
    Another way to think of it is:
    "For every 0, how many 1's does it pass through to get to the right end
    of the array?"
    Solution A: O(log(N))
    From the left, we grab every "0" and move it right, counting the
    number of "1"s it passes, then sum all those counts together.
    This passes every element in the array over every other element
    to its right in the array.
    Solution B: O(N)
    From the left, we count every '0'. When we encounter a '1' we add the
    current count, all the cars going east that will pass this one going west,
    to the total: O(N).
    Lesson:
    When passing over a dataset think about how accumulating metadata about that
    data can reduce the need to see the data again.
    In this example, we accumulate the count of cars going east so that, when
    we encounter a car going west, we can apply the metadata and never look back.
    """
    east = passes = 0
    for direction in A:
        if direction == 0:  # Going East.
            east += 1
        else:  # Going West.
            passes += east
        if passes > MAX_PAIRS:  # They do test for this!
            return -1
    return passes
