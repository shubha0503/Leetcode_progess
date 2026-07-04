# Last updated: 7/4/2026, 10:44:10 AM
class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        position = 0
        max_gap = 0
        
        while n > 0:
            if n & 1:
                if last != -1:
                    max_gap = max(max_gap, position - last)
                last = position
            n >>= 1
            position += 1
        
        return max_gap