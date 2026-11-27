class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        val = list(s)
        window_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u'] 
        for i in range(k):
            if s[i] in vowels:
                window_count += 1
        
        max_count = window_count

        for i in range(k, len(val)):
            if s[i] in vowels:
                window_count += 1
            
            if s[i-k] in vowels:
                window_count -= 1

            if window_count > max_count:
                max_count = window_count

        return max_count

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimal solution implementing algorithms technique.
# Tags: array, optimized

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        val = list(s)
        window_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u'] 
        for i in range(k):
            if s[i] in vowels:
                window_count += 1
        
        max_count = window_count

        if max_count == k:
            return k

        for i in range(k, len(val)):
            if s[i] in vowels:
                window_count += 1
            
            if s[i-k] in vowels:
                window_count -= 1

            if window_count > max_count:
                max_count = window_count

            if max_count == k:
                return k

        return max_count

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimal solution implementing algorithms technique.
# Tags: array, optimized
