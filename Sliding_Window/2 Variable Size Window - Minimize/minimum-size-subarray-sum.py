class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_length = float('inf')
        window_sum = 0

        for right in range(len(nums)):

            window_sum += nums[right]
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1
            
        return 0 if min_length == float('inf') else min_length

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hash Map / Set lookup storing frequencies or previous values for O(1) average-time queries.
# Tags: hashing, sliding-window, optimized
