class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer = []
        n = len(nums)
        prod_tot = 1
        zero_count = 0

        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                continue

            prod_tot *= nums[i]

        for i in range(n):
            if zero_count > 1:
                val = 0

            elif zero_count == 1:
                val = prod_tot if nums[i] == 0 else 0

            else:
                val = prod_tot // nums[i]

            answer.append(val)

        return answer