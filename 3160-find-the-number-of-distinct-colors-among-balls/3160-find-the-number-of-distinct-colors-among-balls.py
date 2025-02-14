from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_to_color = defaultdict(int)
        color_freq = defaultdict(int)
        result = []

        for (ball, color) in queries:
            prev_color = ball_to_color[ball]
            
            if prev_color > 0:
                color_freq[prev_color] -= 1
                if color_freq[prev_color] == 0:
                    del color_freq[prev_color]
            
            ball_to_color[ball] = color
            color_freq[color] += 1

            result.append(len(color_freq))
        
        return result
    
# Time = O(n), Space = O(n) -> O(Limit + 1 + m + q) where limit + 1 is number of balls and m is the number of distinct colors and q is the number of queries (for the result array)
    
sol = Solution()
print("Begin testing...")
assert sol.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]) == [1,2,2,3,4]
assert sol.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]) == [1,2,2,3]
print("End testing...")