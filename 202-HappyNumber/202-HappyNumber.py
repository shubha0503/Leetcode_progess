# Last updated: 11/25/2026, 7:58:09 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0
            n = str(n)
            for d in n:
                d = int(d)
                total += d **2
            n = total
        return True
