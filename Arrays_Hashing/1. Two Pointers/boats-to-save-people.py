class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)

        left = 0
        right = n - 1
        res = 0

        while left <= right:
            total = people[left] + people[right]
            if total > limit:
                right -= 1
                res += 1
            elif total <= limit:
                left += 1
                right -= 1
                res += 1
            
        return res