# Last updated: 7/13/2026, 10:40:17 AM
1class Solution:
2    def sequentialDigits(self, low: int, high: int) -> List[int]:
3        ans = []
4        for i in range(1, 9):
5            x = i
6            for j in range(i + 1, 10):
7                x = x * 10 + j
8                if low <= x <= high:
9                    ans.append(x)
10        return sorted(ans)