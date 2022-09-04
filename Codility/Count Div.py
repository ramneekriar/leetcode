"""
# CountDiv
Compute number of integers divisible by k in range [a..b].
Write a function:
    def solution(A, B, K)
that, given three integers A, B and K, returns the number of integers within the range [A..B] that are
divisible by K, i.e.:
    { i : A <= i <= B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three
numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
Write an efficient algorithm for the following assumptions:
    * A and B are integers within the range [0..2,000,000,000];
    * K is an integer within the range [1..2,000,000,000];
    * A ≤ B.
Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""


def solution(A, B, K):
    """Compute number of integers divisible by k in range [a..b].
    :param A: [int] start
    :param B: [int] end
    :param K: [int] divisor
    :returns: [int] count of integers A..B divisible by K
    This has a mathematical solution:
    Work out the number of times K goes evenly into B.
    Work out the number of times K goes evenly into A.
    But, subtracting one from the other goes wrong when A is exactly divisible
    by K.
    Which we can easily account for that by reducing A by 1 before dividing by K.
    """
    return B // K - (A - 1) // K