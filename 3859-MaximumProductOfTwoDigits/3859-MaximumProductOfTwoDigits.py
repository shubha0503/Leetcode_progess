# Last updated: 7/27/2026, 9:50:54 AM
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