class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = []
        total = 0

        for num in nums:
            total += num
            prefix.append(total)
        
        return prefix

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        return prefix

# Approach: Prefix Sum
