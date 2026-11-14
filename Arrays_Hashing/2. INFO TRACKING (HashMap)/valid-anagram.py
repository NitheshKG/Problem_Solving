class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        val = {}

        for i in range(len(s)):
            val[s[i]] = val.get(s[i], 0) + 1

        for i in t:
            if i not in val:
                return False

            val[i] -= 1

            if val[i] < 0:
                return False
        
        return True