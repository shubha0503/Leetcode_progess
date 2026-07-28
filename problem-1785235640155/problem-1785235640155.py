# Last updated: 7/28/2026, 4:17:20 PM
1class Solution:
2    def smallestPalindrome(self, s: str) -> str:
3        cnt = Counter(s)
4        t = []
5        ch = ""
6        for c in ascii_lowercase:
7            v = cnt[c] // 2
8            t.append(c * v)
9            cnt[c] -= v * 2
10            if cnt[c] == 1:
11                ch = c
12        ans = "".join(t)
13        ans = ans + ch + ans[::-1]
14        return ans