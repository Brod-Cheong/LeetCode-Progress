class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_list=sorted(list(s))
        t_list=sorted(list(t))
        for index,letter in enumerate(s_list):
            if letter == t_list[index]:
                pass
            else:
                return False
        return True
        # return sorted(s) == sorted(t) 
