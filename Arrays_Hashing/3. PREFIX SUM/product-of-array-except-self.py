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

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer