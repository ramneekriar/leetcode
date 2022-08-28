class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                if token == '+':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    result = num1 + num2
                    stack.append(result)
                if token == '-':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    result = num1 - num2
                    stack.append(result)
                if token == '*':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    result = num1 * num2
                    stack.append(result)
                if token == '/':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    result = num1 / num2
                    stack.append(int(result))
        return stack.pop()
    
    def evalRPN2(self, tokens: list[str]) -> int:
        
        #strategy: stacks
        #importants: every input produces a valid output, ie a number.
        """summary: example to keep in mind: 3 4 +      =      3 + 4      = 7
        
        We can only evaluate an expression with two operands and one operator, in that order. Furthermore, the evaluated expression (and value, ie. 7) can be used for more operations and operands, ie. it could be a nested expression like (3+4)+5 = 7+5
        So once we evaluate an expression, that new value is also needed to be kept.
        
        In CS terms:
        
        If any time, we have two operands and then read in an operator, we evaluate that expression. ie, pop/read two elements off the stack, and evaluate. Then push/append that new value to deal with later. 
        """
        
        #SYNTAX PYTHON:
        """Edge case dealings: Floor integer weird, and isnumeric() weird with negatives
        more on:                 #https://stackoverflow.com/questions/37283786/floor-division-with-negative-number#:~:text=That%20means%20that%20the%20result,(performed%20with%20%2F%20operator).&text=7%20%2F%202%20%3D%203.5%20so%207,of%20%2D3.5%20%3D%20%2D4%20.
        """
        #Stack syntax. Instead of push and pop, python's methods are:
        #push == append()
        #pop == pop()
        
        returnable = list()
        
        for token in tokens:
            if token.isnumeric() or token[-1]!= token[0]: #stupid edge case, 11 is numeric. -11 is not.
                returnable.append(token)
                continue
            else: #is operator
                val2 = returnable.pop()
                val1 = returnable.pop()
                

                if token == "/":
                    newVal = str(int(int(val1) / int(val2)))
                else:
                    newVal = str(eval(str(val1) + token + str(val2)))

                returnable.append(newVal)
                
        return returnable[0] #last element in stack is our value :)