# Last updated: 9/16/2026, 11:51:52 AM
class Solution:
    def maxProduct(self, n: int) -> int:
        a = b = 0
        while n:
            n, x = divmod(n, 10)
            if a < x:
                a, b = x, a
            elif b < x:
                b = x
        return a * b