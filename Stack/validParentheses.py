class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    
    def matchingParenthesis(self, s: str) -> list:
        open_bracket = {'{', '[', '('}
        close_bracket = {'}', ']', ')'}
        bracket_dict = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if c in open_bracket:
                stack.append(c)
            elif c in close_bracket:
                if not stack:
                    return 'NO'
                elif bracket_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return 'NO'
            else:
                return 'NO'
        if stack:
            return 'NO'
        return 'YES'