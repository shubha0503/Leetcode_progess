# Last updated: 10/7/2026, 11:19:05 PM
1class Solution:
2    def removeInvalidParentheses(self, s: str) -> List[str]:
3        def dfs(i, l, r, lcnt, rcnt, t):
4            if i == n:
5                if l == 0 and r == 0:
6                    ans.add(t)
7                return
8            if n - i < l + r or lcnt < rcnt:
9                return
10            if s[i] == '(' and l:
11                dfs(i + 1, l - 1, r, lcnt, rcnt, t)
12            elif s[i] == ')' and r:
13                dfs(i + 1, l, r - 1, lcnt, rcnt, t)
14            dfs(i + 1, l, r, lcnt + (s[i] == '('), rcnt + (s[i] == ')'), t + s[i])
15
16        l = r = 0
17        for c in s:
18            if c == '(':
19                l += 1
20            elif c == ')':
21                if l:
22                    l -= 1
23                else:
24                    r += 1
25        ans = set()
26        n = len(s)
27        dfs(0, l, r, 0, 0, '')
28        return list(ans)