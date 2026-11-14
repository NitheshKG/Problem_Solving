class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        val = {}

        for i in magazine:
            val[i] = val.get(i, 0) + 1
        
        for i in ransomNote:
            if i not in val:
                return False
            
            val[i] -= 1

            if val[i] < 0:
                return False

        return True