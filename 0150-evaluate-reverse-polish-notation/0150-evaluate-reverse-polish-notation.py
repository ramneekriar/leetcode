from secrets import token_urlsafe


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2 - temp1)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t== '/':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(int(temp2 / temp1))
            else:
                stack.append(int(t))
        
        return stack[0]