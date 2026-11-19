class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0

        def expand(left, right):
            nonlocal start, end

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > end - start:
                    start = left
                    end = right
                
                left -= 1
                right += 1
            
        for i in range(n):
            expand(i, i)

            expand(i, i+1)

        return s[start:end +1]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Sliding Window maintaining a valid window invariant by dynamically expanding right and contracting left.
# Tags: sliding-window, optimized
