class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        unique=set(nums)
        for i in unique:
            dictionary[i]=nums.count(i)
    
        return sorted(dictionary.keys(),key=lambda x:dictionary[x],reverse=True)[:k]