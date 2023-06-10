class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in tokens:
      
            
            if i == "+":
                first_val=int(stack.pop())
                second_val=int(stack.pop())
                stack.append(second_val+first_val)
            elif i== "-":
                first_val=int(stack.pop())
                second_val=int(stack.pop())
                stack.append(second_val-first_val)
            elif i=='*':
                first_val=int(stack.pop())
                second_val=int(stack.pop())
                stack.append(second_val*first_val)
            elif i =="/":
                first_val=int(stack.pop())
                second_val=int(stack.pop())
                stack.append(second_val/first_val)
            else:
                stack.append(i)
        return int(stack.pop())
