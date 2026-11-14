class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_t = {}
        t_s = {}

        for i, j in zip(s, t):

            if i in s_t and s_t[i] != j:
                return False
            
            if j in t_s and t_s[j] != i:
                return False

            s_t[i] = j
            t_s[j] = i
        
        return True