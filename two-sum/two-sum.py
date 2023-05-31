# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for x in range(len(nums)):

#                 if (nums[i]+nums[x])== target and i!=x:
              
#                     return [i,x]
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            dic[num] = i
        # print(dic)
        for i in range(len(nums)):
            complement = target - nums[i] # 9 - 2 = 7
            if complement in dic and dic[complement] != i:
                return [dic[complement],i]





# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_dict={k: v for v, k in enumerate(nums)}
#         copy_nums=nums
#         for i in range(len(nums)):  
#             current_number=nums[i]
#             for x in range(len(copy_nums)):
#                 if (nums[i]+copy_nums[x])== target and i!=nums_dict.get(copy_nums[x]):
                
#                     return [i,nums_dict.get(copy_nums[x])]
#             copy_nums=copy_nums[i+1:]
                


























                    
     