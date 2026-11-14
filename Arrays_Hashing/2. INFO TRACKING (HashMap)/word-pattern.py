class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split()):
            return False
            
        p_s = {}
        s_p = {}

        for i, j in zip(pattern, s.split()):
            
            if i in p_s and p_s[i] != j:
                return False

            if j in s_p and s_p[j] != i:
                return False
            
            p_s[i] = j
            s_p[j] = i

        return True