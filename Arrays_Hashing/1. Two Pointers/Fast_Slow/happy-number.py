class Solution:
    def isHappy(self, n: int) -> bool:

        def getNext(n):
            if n == 0:
                return 0

            total = n % 10
            val = n // 10

            return total ** 2 + getNext(val)

        slow = n
        fast = n

        while True:
            slow = getNext(slow)

            fast = getNext(fast)
            fast = getNext(fast)

            if fast == 1:
                return True
            elif slow == fast:
                return False