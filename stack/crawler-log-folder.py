class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0

        for i in logs:
            if i == "../":
                count -= 1
            elif i == "./":
                continue
            else:
                count += 1

            if count < 0:
                count = 0
        
        return count

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Monotonic Stack / LIFO tracking to process matching boundaries and maintain ordered candidates.
# Tags: stack, optimized
