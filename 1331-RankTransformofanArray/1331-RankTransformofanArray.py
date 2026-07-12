# Last updated: 7/12/2026, 10:20:22 PM
1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        t = sorted(set(arr))
4        return [bisect_right(t, x) for x in arr] 