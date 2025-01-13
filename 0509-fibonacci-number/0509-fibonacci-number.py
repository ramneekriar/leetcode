class Solution:
    # Recursive Approach
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# Time = O(2^n) because we are creating 2 branches for each call and n is the height of the tree
# Space = O(n)

    # Memoization
    memo = {0:0, 1:1}
    def fibMemo(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.fibMemo(n - 1) + self.fibMemo(n - 2)
        return self.memo[n]

# Time = O(n) since we are only doing one calculation for each number that we encounter, only following down one branch
# Space = O(n)