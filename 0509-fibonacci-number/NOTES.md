<h2><a href="https://leetcode.com/problems/fibonacci-number/description/">509. Fibonacci Number</a></h2><h3>Easy</h3>

<h3>Optimal Approach - Bottom Up DP with 2 variables</h3>
<p>In this optimal approach, we first initalize the base cases and return n. Otherwise, create variable a=0 and b=1 for the two base cases. Iterate over from index 2 to (n + 1), and calculate the new fib_num by doing a + b. Then we need to update our a and b variables. To do this, you can do this concurrently by assigning b's value to a and the new fib_num value to b at the same time. At the end of the iteration, return the number in fib_num.</p>

<h3>Tabulation Approach - Bottom Up DP</h3>
<p>In the tabulation approach, we create a list filled with 0s with a size of (n + 1). Then we can initialize the base cases, and fill the list at index 0 and 1 with those. If n happens to be less than or equal to 1, then simply return n. Otherwise, from index 2 to (n + 1), simply calculate the fibonacci number for that index by adding the previous two numbers in the list. At the end of the iteration, return the number in the list at index n.</p>

<h3>Recursive</h3>
<p>Create the base case first which will be if n is smaller or equal to 1, then just return n. That's because we know that in the fibonacci sequence it starts with f(0) = 0 and f(1) = 1. For the recursive case, we will be returning self.fib(n - 1) + self.fib(n - 2). This will basically keep making function calls until we hit a base case and add the results on the way up the recursive branches.</p>

<h3>Memoization - Top Down DP</h3>
<p>Create a memo dictionary to hold the results of the calculations. I chose to store the base case for 0 and 1 in the memo dict so that I don't need to do a specific if n <= 1 check again in the function. Check if n is in our memo dict. If so, return self.memo[n] since we have the calculation already stored. Otherwise, in self.memo[n] store the result of the recursive call of (n - 1) + (n - 2). Return self.memo[n].</p>
