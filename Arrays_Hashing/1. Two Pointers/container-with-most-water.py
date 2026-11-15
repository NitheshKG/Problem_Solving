class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        result = 0

        while left < right:
            total = (right - left) * min(height[left], height[right])

            if total > result:
                result = total
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result