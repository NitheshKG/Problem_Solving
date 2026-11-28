class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_map = {}
        window_map = {}

        for char in t:
            target_map[char] = target_map.get(char, 0) + 1

        left = 0
        formed = 0
        required = len(target_map)

        min_length = float('inf')
        start_index = 0

        for right in range(len(s)):

            char = s[right]
            window_map[char] = window_map.get(char, 0) + 1

            if char in target_map and window_map[char] == target_map[char]:
                formed += 1

            while formed == required:

                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    start_index = left

                left_char = s[left]

                if left_char in target_map and window_map[left_char] == target_map[left_char]:
                    formed -= 1

                window_map[left_char] -= 1
                left += 1

        if min_length == float('inf'):
            return ""

        return s[start_index:start_index + min_length]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Sliding Window maintaining a valid window invariant by dynamically expanding right and contracting left.
# Tags: sliding-window, optimized
