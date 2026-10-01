# Last updated: 10/1/2026, 7:14:23 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stk = []
4        d = {'(': ')', '[': ']', '{': '}'}
5        for c in s:
6            if c in d:
7                stk.append(d[c])
8            elif not stk or stk.pop() != c:
9                return False
10        return not stk