class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        def expand(left, right):
            nonlocal count

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1


        for i in range(n):
            expand(i, i)

            expand(i, i+1)
        
        return count

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimal solution implementing algorithms technique.
# Tags: array, optimized
