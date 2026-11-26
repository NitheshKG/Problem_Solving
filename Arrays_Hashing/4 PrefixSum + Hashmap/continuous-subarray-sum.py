class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefixsum = 0
        count = 0
        val = {0: -1}

        for i in range(len(nums)):
            prefixsum += nums[i]
            rem = prefixsum % k

            if rem in val:
                max_len = i - val[rem]
                if max_len >= 2:
                    return True
            else:
                val[rem] = i

        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hash Map / Set lookup storing frequencies or previous values for O(1) average-time queries.
# Tags: hashing, sliding-window, optimized

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_sum = 0
        val = {0: -1}
        rem = 0
        max_len = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            rem = prefix_sum % k

            if rem in val:
                max_len = i - val[rem]
                if max_len >= 2:
                    return True

            else:
                val[rem] = i

        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hash Map / Set lookup storing frequencies or previous values for O(1) average-time queries.
# Tags: hashing, sliding-window, optimized
