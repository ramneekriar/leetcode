import math
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = [ (math.sqrt(math.pow(x, 2) + math.pow(y, 2)), x, y) for x, y in points]
        heapq.heapify(minHeap)

        i = 0
        output = []
        while i < k:
            distance, x, y = heapq.heappop(minHeap)
            output.append([x, y])
            i += 1
        
        return output

# Time = O(k log N) because we are popping k times and each time the heap has to sort itself/re-heapify causing log n
# Space = O(N + k) because we are storing all n points in minHeap and k is the size of our output array
