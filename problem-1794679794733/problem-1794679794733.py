# Last updated: 11/14/2026, 11:39:54 PM
1
2class Solution:
3    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
4
5        ans = float('inf')
6
7        for i in range(len(nums)):
8            total = 0
9
10            for j in range(i, len(nums)):
11                total += nums[j]
12
13                length = j - i + 1
14
15                if l <= length <= r and total > 0:
16                    ans = min(ans, total)
17
18        if ans == float('inf'):
19            return -1
20
21        return ans
22