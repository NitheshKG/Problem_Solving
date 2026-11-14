class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = []
        total = 0

        for num in nums:
            total += num
            prefix.append(total)
        
        return prefix