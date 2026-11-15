class Solution:
    def minimumSteps(self, s: str) -> int:
        read = 0
        write = 0
        count = 0

        for i in s:
            if i == '0':
                count += read - write
                write += 1
            read += 1
        
        return count