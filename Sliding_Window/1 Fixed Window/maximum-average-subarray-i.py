class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0
        max_val = 0
        for i in range(k):
            window_sum += nums[i]
        
        max_val = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]

            if window_sum > max_val:
                max_val = window_sum

        return max_val/k

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Sliding Window maintaining a valid window invariant by dynamically expanding right and contracting left.
# Tags: sliding-window, optimized
