class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1set = set(nums1)
        nums2set = set(nums2)

        return list(nums1set.intersection(nums2set))