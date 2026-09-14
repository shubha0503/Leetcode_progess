# Last updated: 9/14/2026, 5:29:24 PM
1class Solution:
2    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
3        x1, y1, x2, y2 = rec1
4        x3, y3, x4, y4 = rec2
5        return not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)