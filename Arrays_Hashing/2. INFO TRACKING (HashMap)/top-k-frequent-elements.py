class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = {}

        for num in nums:
            res[num] = res.get(num, 0) + 1

        sorted_dict = dict(sorted(res.items(), key= lambda x: x[1], reverse= True))
        key_val = list(sorted_dict.keys())
        
        return key_val[:k]