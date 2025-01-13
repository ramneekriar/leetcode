class Solution:
    # Recursive Approach
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    # Memoization
    memo = {0:0, 1:1}
    def fibMemo(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.fibMemo(n - 1) + self.fibMemo(n - 2)
        return self.memo[n]