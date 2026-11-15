class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        val_list = list(s)
        n = len(val_list)
        
        for i in range(0, n, 2*k):
            left = i
            right = min(i + k - 1, n-1)
            while left < right:
                val_list[left], val_list[right] = val_list[right], val_list[left]
                left += 1
                right -= 1

        return "".join(val_list)