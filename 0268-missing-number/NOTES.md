<h2><a href="https://leetcode.com/problems/missing-number/">268. Missing Number</a></h2><h3>Easy</h3>

<p>The first approach we can do is a bitwise XOR. We initialize result with len(nums) because the missing number is not going to be XORed in the loop, but the index will be. This takes care of the missing index for that number since we are looping from index 0 to (n - 1). Then we enumerate over nums, getting both the index and the number. We store the xor between result, the index and current num into result and return that after exiting the loop.</p>

<p>Example: nums = [3, 0, 1] and the missing number is 2. We initialize result with len(nums) which is 3. Then we xor over the numbers and indices of nums. That will look like this: 3^3^0 = 0, 0^0^1 = 1, 1^2^1 = 2. Therefore, the missing number is 2.<p>

<p>Another way is to use the summation formula to sum all numbers from 0 to n: n(n+1)/2. This way we can calculate the expected sum and subtract the actual sum of the given array from it and return the result.</p>
