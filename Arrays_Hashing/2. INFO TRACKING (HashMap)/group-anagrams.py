class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for val in strs:
            key = "".join(sorted(val))
            anag[key] = anag.get(key, [])
            anag[key].append(val)

        # print(anag)
        
        return list(anag.values())