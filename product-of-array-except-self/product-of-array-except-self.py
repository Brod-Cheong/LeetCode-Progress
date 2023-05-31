class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
        # "len(nums) - 1" is the starting point of the sequence. It represents the index of the last element in the list or iterable object "nums". The "-1" is used because indexing in Python starts from 0, so this expression gets the index of the last element.

        # "-1" is the stop value of the sequence. It specifies the value at which the sequence will stop generating numbers. In this case, it stops at -1, inclusive.

        # "-1" is the step value, which determines the increment or decrement between consecutive numbers in the sequence. In this case, it is set to -1, indicating that the numbers will be generated in descending order, decrementing by 1 each time.
            res[i] *= postfix
            postfix *= nums[i]
        return res
