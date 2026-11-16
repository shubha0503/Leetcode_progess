# Last updated: 11/16/2026, 10:00:53 PM
1class Solution:
2    def maxArea(self, height: list[int]) -> int:
3        left = 0
4        maxi = 0
5        right = len(height) - 1
6        while left < right:
7            width = right - left
8            area = width * min(height[left],height[right])
9            maxi = max(area,maxi)
10            if height[left] < height[right]:
11                left += 1
12            else:
13                right -= 1
14        return maxi
15
16
17    
18        