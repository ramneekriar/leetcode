<h2><a href="https://leetcode.com/problems/fibonacci-number/description/">509. Fibonacci Number</a></h2><h3>Easy</h3>

<h3>Recursive</h3>
<p>Create the base case first which will be if n is smaller or equal to 1, then just return n. That's because we know that in the fibonacci sequence it starts with f(0) = 0 and f(1) = 1. For the recursive case, we will be returning self.fib(n - 1) + self.fib(n - 2). This will basically keep making function calls until we hit a base case and add the results on the way up the recursive branches.</p>

<h3>Memoization</h3>
<p>Create a memo dictionary to hold the results of the calculations. I chose to store the base case for 0 and 1 in the memo dict so that I don't need to do a specific if n <= 1 check again in the function. Check if n is in our memo dict. If so, return self.memo[n] since we have the calculation already stored. Otherwise, in self.memo[n] store the result of the recursive call of (n - 1) + (n - 2). Return self.memo[n].</p>
