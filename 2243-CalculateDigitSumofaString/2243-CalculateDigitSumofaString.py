# Last updated: 11/16/2026, 9:47:37 PM
1class Solution:
2    def digitSum(self, s: str, k: int) -> str:
3        while len(s) > k:
4            new_s = ""
5            for i in range(0,len(s),k):
6                group = s[i:i+k]
7                total = sum(int(ch) for ch in group )
8                new_s += str(total)
9            s = new_s
10        return s