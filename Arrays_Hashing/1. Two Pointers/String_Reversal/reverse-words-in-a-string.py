class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        val_list = s.split()
        # print(val_list)
        
        left = 0
        right = len(val_list) - 1

        while left < right:
            val_list[left], val_list[right] = val_list[right], val_list[left]
            left += 1
            right -= 1
        
        return " ".join(val_list)