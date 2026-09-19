# Last updated: 9/19/2026, 11:37:48 PM
1class Solution:
2    def checkOverlap(
3        self,
4        radius: int,
5        xCenter: int,
6        yCenter: int,
7        x1: int,
8        y1: int,
9        x2: int,
10        y2: int,
11    ) -> bool:
12        def f(i: int, j: int, k: int) -> int:
13            if i <= k <= j:
14                return 0
15            return i - k if k < i else k - j
16
17        a = f(x1, x2, xCenter)
18        b = f(y1, y2, yCenter)
19        return a * a + b * b <= radius * radius