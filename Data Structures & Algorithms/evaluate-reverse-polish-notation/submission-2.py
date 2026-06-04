'''
- we want to preserve order and get the latest tokens: 
    - points me towards a stack 
- iterate through the list of tokens: 
    - whenver a number is encountered, then push it onto the stack 
    - when an operand is encountered: 
        - do the operation 
        - push the number on to the stack 

- for the final solution, pop the last element of the stack 
    
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ## for stack behavior, we use an array 

        stack = [] 

        operators = {"+", "-", "*", "/"}

        for token in tokens: 
            if token in operators: 
                if token == "+" : 
                    num_1 = stack.pop() 
                    num_2 = stack.pop() 

                    stack.append(num_1 + num_2)
                
                if token == "-": 
                    num_1 = stack.pop() 
                    num_2 = stack.pop() 

                    stack.append(num_2 - num_1)

                if token == "*": 
                    num_1 = stack.pop() 
                    num_2 = stack.pop()

                    stack.append(num_1 * num_2)
                
                if token == "/": 
                    num_1 = stack.pop() 
                    num_2 = stack.pop() 

                    stack.append(int(num_2 / num_1))

            else: 
                stack.append(int(token))

        
        return stack.pop()

        