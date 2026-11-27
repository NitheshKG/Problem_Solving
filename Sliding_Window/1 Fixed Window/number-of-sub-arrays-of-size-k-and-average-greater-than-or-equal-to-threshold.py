class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = 0
        count = 0
        for i in range(k):
            window_sum += arr[i]

        if window_sum / k >= threshold:
            count += 1
        
        max_val = count

        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]

            if window_sum / k >= threshold:
                count += 1
                if count > max_val:
                    max_val = count

        return max_val

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimal solution implementing algorithms technique.
# Tags: array, optimized
