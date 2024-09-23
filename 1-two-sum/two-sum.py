class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for index,x in enumerate(nums):
            pair_number=target-x
            if pair_number in hashmap:
                return [index,hashmap[pair_number]]
            hashmap[x]=index