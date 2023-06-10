class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in tokens:
      
            
            if i == "+":
                
                stack.append(stack.pop()+stack.pop())
            elif i== "-":
                first_val=(stack.pop())
                second_val=(stack.pop())
                stack.append(second_val-first_val)
            elif i=='*':
                
                stack.append(stack.pop()*stack.pop())
            elif i =="/":
                first_val=(stack.pop())
                second_val=(stack.pop())
                stack.append(int(second_val/first_val))
            else:
                stack.append(int(i))
        return stack[0]
