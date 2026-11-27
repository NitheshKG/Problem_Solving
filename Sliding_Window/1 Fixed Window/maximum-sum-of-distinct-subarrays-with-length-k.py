class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:

        window_sum = 0
        max_val = 0
        val = {}

        for i in range(k):
            window_sum += nums[i]
            val[nums[i]] = val.get(nums[i], 0) + 1

        if len(val) == k:
            max_val = window_sum

        for i in range(k, len(nums)):

            window_sum -= nums[i-k]
            val[nums[i-k]] -= 1

            if val[nums[i-k]] == 0:
                del val[nums[i-k]]

            window_sum += nums[i]
            val[nums[i]] = val.get(nums[i], 0) + 1

            # Check if all elements are distinct
            if len(val) == k:
                if window_sum > max_val:
                    max_val = window_sum

        return max_val

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimal solution implementing algorithms technique.
# Tags: array, optimized
