class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique= set(nums)
        longest=0
        for i in nums:

            if (i-1)not in unique:
                curr_len=1
                next_num=i+1
                while next_num in unique:
                    curr_len+=1
                    next_num+=1
                longest=max(longest,curr_len)
        return longest