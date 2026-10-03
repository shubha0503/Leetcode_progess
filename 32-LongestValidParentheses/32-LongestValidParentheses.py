# Last updated: 10/3/2026, 9:50:55 PM
1class Solution:
2  def longestValidParentheses(self, s: str) -> int:
3    s2 = ')' + s
4    # dp[i] := the length of the longest valid parentheses in the substring
5    # s2[1..i]
6    dp = [0] * len(s2)
7
8    for i in range(1, len(s2)):
9      if s2[i] == ')' and s2[i - dp[i - 1] - 1] == '(':
10        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
11
12    return max(dp)