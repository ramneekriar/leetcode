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

    def matchingParenthesis2(self, s: list[str]) -> list[str]:
        stack = []
        result = []
        bracket_dict = {"}": "{", "]": "[", ")": "("}
        for braceSet in s:
            for char in braceSet:
                if char in {'{', '[', '('}:
                    stack.append(char)
                elif char in {'}', ']', ')'}:
                    if not stack:
                        result.append('NO')
                    elif bracket_dict[char] == stack[-1]:
                        stack.pop() 
                    else:
                        result.append('NO')
                else:
                    result.append('NO')
            if stack:
                result.append('NO')
            else:
                result.append('YES')

            stack = []
        return result

if __name__ == '__main__':
    s = Solution()
    ans = s.matchingParenthesis2(["[]()[[()]]", "()(", "[][][]"])
    print(ans)
