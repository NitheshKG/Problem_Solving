class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            is_neg = True
        val_list = list(str(abs(x)))
        
        left = 0
        right = len(val_list) - 1



        while left < right:
            val_list[left], val_list[right] = val_list[right], val_list[left]
            left += 1
            right -= 1
        
        val = int("".join(val_list))
        
        if is_neg:
            val = -val

        if -2**31 < val < 2**31:
            return val
        else:
            return 0