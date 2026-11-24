# Last updated: 11/24/2026, 10:59:21 PM
1import math
2
3
4class Solution:
5
6  def maxLength(self, nums: list[int]) -> int:
7    n = len(nums)
8    ans = 0
9
10    for i in range(n):
11      prod = 1
12      g = 0
13      l = 1
14      for j in range(i, n):
15        x = nums[j]
16        prod *= x
17        g = math.gcd(g, x)
18        l = math.lcm(l, x)
19
20        if prod == g * l:
21          ans = max(ans, j - i + 1)
22
23    return ans