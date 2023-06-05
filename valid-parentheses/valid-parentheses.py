class Solution:
    def isValid(self, s: str) -> bool:
        brac_dict={
            "{": "}",
            "(":")",
            "[":"]"

        }
        
        #this only works for "{}(){}" not "[()]"
        # for idx, i in enumerate(s):
        #     if i in brac_dict.keys(): #if is a opening bracket
        #         if  brac_dict[i]== s[idx+1]: #check for closing bracket
        #             continue
        #         else:
        #             return False
        #     else:
        #         pass
        # return True
        stack=[]
        for i in s:
            if i in brac_dict:
                stack.append(i)
            elif not stack or i != brac_dict[stack.pop()]:
                return False

        return not stack

