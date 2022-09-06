class Solution:
    def hammingWeight(self, n: int) -> int:
        N = bin(n)[2:]
        count = 0
        for i in N:
            if i == '1':
                count += 1
        return count
    
    def hammingWeight2(self, n: int) -> int:
        count = 0
        for i in str(bin(n)):
            if i == '1':
                count += 1
        return count