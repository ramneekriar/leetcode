class Solution:
    def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i, (start, end) in enumerate(intervals):
            # insert interval comes before current interval
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            
            # insert interval comes after current interval
            if newInterval[0] > end:
                res.append(intervals[i])
            
            # insert interval overlaps with current interval
            else:
                # merge
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
            
        
        res.append(newInterval)
        return res

# Time = O(n)
# Space = O(n)