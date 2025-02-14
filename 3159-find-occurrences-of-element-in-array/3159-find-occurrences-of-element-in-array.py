class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        # nums -> list[int]
        # queries -> list[int]
        # x = int

        # need to find index of queries[i]th occurrence of x in nums
        # if there are fewer than queries[i] occurrences of x, ans should be -1
        # return answer 

        # nums = [1, 3, 1, 7]
        # queries = [1, 3, 2, 4]
        # x = 1
        # result = [0, -1, 2, -1]

        # How many occurrences of x? there are 2 occ of 1

        positions = [] # all indices of x where i is occurrence number and num is the actual index
        answer = []
        num_occurrences = 0 # total num occurrences of x

        for (index, num) in enumerate(nums):
            if num == x:
                num_occurrences += 1
                positions.append(index)
        
        for q in queries:
            if q > num_occurrences:
                answer.append(-1)
            else:
                answer.append(positions[q - 1])
        
        return answer

# Time = O(n), Space = O(n) -> O(p + a) where p is number of positions of x and a is the size of answer array

sol = Solution()
print("Begin testing...")
assert sol.occurrencesOfElement([1,3,1,7], [1,3,2,4], 1) == [0,-1,2,-1]
assert sol.occurrencesOfElement([1,2,3], [10], 5) == [-1]
print("End testing...")
