class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        val_1 = list(word1)
        val_2 = list(word2)
        n1 = len(word1)
        n2 = len(word2)
        word = []

        while i < n1 and j < n2:
            word.append(val_1[i])
            word.append(val_2[j])
            i += 1
            j += 1

        res = "".join(word)
        if n1 > n2:
            res += word1[i:]
        elif n1 < n2:
            res += word2[j:]

        return res