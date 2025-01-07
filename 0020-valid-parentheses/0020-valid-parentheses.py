class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {'}':'{', ']':'[', ')':'('}
        stack = []

        for bracket in s:
            if bracket not in close_to_open:
                stack.append(bracket)
            else:
                if stack and stack[-1] == close_to_open[bracket]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False # Or can do return stack == []

# Time = O(n), Space = O(n)