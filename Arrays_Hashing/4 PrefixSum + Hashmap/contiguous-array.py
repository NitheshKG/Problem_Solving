class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        val = [-1 if i == 0 else 1 for i in nums]

        for i in range(n):
            prefix[i] = prefix[i-1] + val[i]

        res = {0 : -1}
        max_len = 0
        print(prefix)

        # for i in range(n):
        #     if prefix[i] in res:
        #         max_len = max(max_len, i - res[prefix[i]])
        #     else:
        #         res[prefix[i]] = i
            
        for i in range(n):
            if prefix[i] in res:
                max_len = max(max_len, i - res[prefix[i]])
            else:
                res[prefix[i]] = i
        return max_len

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Sliding Window maintaining a valid window invariant by dynamically expanding right and contracting left.
# Tags: sliding-window, optimized
