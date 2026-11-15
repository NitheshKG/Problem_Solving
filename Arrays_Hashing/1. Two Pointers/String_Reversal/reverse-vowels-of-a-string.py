class Solution:
    def reverseVowels(self, s: str) -> str:
        val_list = list(s)
        n = len(val_list)

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        left = 0
        right = n - 1

        while left < right:
            if val_list[left] not in vowels:
                left += 1
            
            if val_list[right] not in vowels:
                right -= 1

            elif val_list[left] in vowels and val_list[right] in vowels:
                val_list[left], val_list[right] = val_list[right] , val_list[left]
                left += 1
                right -= 1
        
        return "".join(val_list)