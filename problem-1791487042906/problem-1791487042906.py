# Last updated: 10/9/2026, 12:47:22 AM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        ans = []
4        cnt = 0
5        for c in s:
6            if c == '(':
7                cnt += 1
8                if cnt > 1:
9                    ans.append(c)
10            else:
11                cnt -= 1
12                if cnt > 0:
13                    ans.append(c)
14        return ''.join(ans)