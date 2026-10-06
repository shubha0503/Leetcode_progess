# Last updated: 10/7/2026, 3:23:29 AM
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        stk = []
4        for c in s:
5            if c == ')' and stk and stk[-1] == '(':
6                stk.pop()
7            else:
8                stk.append(c)
9        return len(stk)