# Last updated: 8/12/2026, 11:41:04 PM
1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        ans = l = 0
4        cnt = defaultdict(int)
5        for r, x in enumerate(nums):
6            cnt[x] += 1
7            while cnt[x] > k:
8                cnt[nums[l]] -= 1
9                l += 1
10            ans = max(ans, r - l + 1)
11        return ans