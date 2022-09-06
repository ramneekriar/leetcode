# Python given an array A of N integers, returns the smallest positive 
# integer (greater than 0) that does not occur in A in O(n) time complexity

def minpositive(a):
    A = set(a) # --> converts everything into set, no duplicates
    ans = 1 # --> the smallest possible positive integer
    while ans in A: # --> while int exists in set A, keep adding 1 to it
       ans += 1
    return ans # loop breaks and returns smallest positive integer that does not exist in array