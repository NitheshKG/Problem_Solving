class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        val = {}
        for i , num in enumerate(nums):
            total = target - num
            if total in val:
                return [val[total], i]
            val[num] = i
        
        return []