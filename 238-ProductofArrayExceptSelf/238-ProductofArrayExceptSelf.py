# Last updated: 11/11/2026, 11:44:18 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3
4        n = len(nums)
5
6        prefix = [1] * n
7        suffix = [1] * n
8        ans = [1] * n
9
10        for i in range(1, n):
11            prefix[i] = prefix[i-1] * nums[i-1]
12
13        for i in range(n-2, -1, -1):
14            suffix[i] = suffix[i+1] * nums[i+1]
15
16        for i in range(n):
17            ans[i] = prefix[i] * suffix[i]
18
19        return ans