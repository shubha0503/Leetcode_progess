# Last updated: 9/28/2026, 12:24:39 AM
1class Solution:
2    def reverseParentheses(self, s: str) -> str:
3        stk = []
4        for c in s:
5            if c == ")":
6                t = []
7                while stk[-1] != "(":
8                    t.append(stk.pop())
9                stk.pop()
10                stk.extend(t)
11            else:
12                stk.append(c)
13        return "".join(stk)