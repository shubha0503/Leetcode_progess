# Last updated: 11/13/2026, 10:16:01 PM
1class Solution:
2    def longestPalindrome(self, s):
3        if not s:
4            return ""
5        
6        start = 0
7        end = 0
8        
9        def expand(left, right):
10            while left >= 0 and right < len(s) and s[left] == s[right]:
11                left -= 1
12                right += 1
13            return right - left - 1
14        
15        for i in range(len(s)):
16            len1 = expand(i, i)       # odd length
17            len2 = expand(i, i + 1)   # even length
18            max_len = max(len1, len2)
19            
20            if max_len > end - start:
21                start = i - (max_len - 1) // 2
22                end = i + max_len // 2
23        
24        return s[start:end + 1]