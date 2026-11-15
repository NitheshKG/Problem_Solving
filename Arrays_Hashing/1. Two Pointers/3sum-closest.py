class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(res - target):
                    res = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return res