class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        val = {0: 1}
        count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            rem = prefix_sum % k

            if rem in val:
                count += val[rem]

            val[rem] = val.get(rem, 0) + 1
        
        return count

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hash Map / Set lookup storing frequencies or previous values for O(1) average-time queries.
# Tags: hashing, optimized
