class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        prod_val = 1
        count = 0
        
        if k <= 1:
            return 0

        for right in range(len(nums)):
            prod_val *= nums[right]

            while prod_val >= k:
                prod_val //= nums[left]
                left += 1
            
            count += right - left + 1

        return count

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Sliding Window maintaining a valid window invariant by dynamically expanding right and contracting left.
# Tags: sliding-window, optimized
