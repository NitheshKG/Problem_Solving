class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0 
        count = 0
        val = {0:1}
        rem = 0

        for i in nums:
            prefix_sum += i
            rem = prefix_sum - k

            if rem in val:
                count += val[rem]

            val[prefix_sum] = val.get(prefix_sum, 0) + 1
        
        return count

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hash Map / Set lookup storing frequencies or previous values for O(1) average-time queries.
# Tags: hashing, optimized
