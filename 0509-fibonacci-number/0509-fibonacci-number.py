class Solution:

    # DP optimal approach with two variables
    def fib_optimal(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            # base cases
            a = 0
            b = 1

            for i in range(2, (n + 1)):
                fib_num = a + b # calculating current fib_num using prev 2 number sums
                a, b = b, fib_num # updating values, a is pointing to prev value of b, and b points to current fib_num calculated in the sequence

            return fib_num

# Time = O(n), Space = O(1)

    # Tabulation Approach -> Bottom Up DP
    def fib_tab(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            fib_list = [0] * (n + 1)
            for i in range(2, (n + 1)):
                fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
            
            return fib_list[n]

# Time = O(n) as we are iterating over every element, Space = O(n)
        
     # Memoization -> Top Down DP
    memo = {0:0, 1:1}
    def fibMemo(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.fibMemo(n - 1) + self.fibMemo(n - 2)
        return self.memo[n]

# Time = O(n) since we are only doing one calculation for each number that we encounter, only following down one branch
# Space = O(n)
        
    # Recursive Approach
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# Time = O(2^n) because we are creating 2 branches for each call and n is the height of the tree
# Space = O(n)