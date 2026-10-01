# Last updated: 10/1/2026, 7:16:29 PM
1class Solution:
2    def braceExpansionII(self, expression: str) -> List[str]:
3        def dfs(exp):
4            j = exp.find('}')
5            if j == -1:
6                s.add(exp)
7                return
8            i = exp.rfind('{', 0, j)
9            a, c = exp[:i], exp[j + 1 :]
10            for b in exp[i + 1 : j].split(','):
11                dfs(a + b + c)
12
13        s = set()
14        dfs(expression)
15        return sorted(s)