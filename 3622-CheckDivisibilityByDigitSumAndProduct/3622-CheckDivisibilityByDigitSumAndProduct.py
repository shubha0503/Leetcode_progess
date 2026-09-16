# Last updated: 9/16/2026, 11:51:41 AM
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p = 0, 1
        x = n
        while x:
            x, v = divmod(x, 10)
            s += v
            p *= v
        return n % (s + p) == 0