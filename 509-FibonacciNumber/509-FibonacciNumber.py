# Last updated: 9/16/2026, 11:59:24 AM
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        a, b = 0, 1

        for _ in range(1, n):
            a, b = b, a + b

        return b