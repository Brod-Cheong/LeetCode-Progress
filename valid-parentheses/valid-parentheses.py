class Solution:
    def isValid(self, s: str) -> bool:
        brac_dict={
            "{": "}",
            "(":")",
            "[":"]"

        }
        
        stack=[]
        for i in s:
            if i in brac_dict:
                stack.append(i)
            elif not stack or i != brac_dict[stack.pop()]:
                return False

        return not stack

