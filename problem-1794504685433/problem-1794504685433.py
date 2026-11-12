# Last updated: 11/12/2026, 11:01:25 PM
1class Solution:
2    def longestMonotonicSubarray(self, nums: List[int]) -> int:
3        icount = 1
4        dcount = 1
5        count = 1
6        for i in range(len(nums)-1):
7            if nums[i] < nums[i+1]:
8                icount += 1
9                dcount = 1
10            elif nums[i] > nums[i+1]:
11                dcount += 1
12                icount = 1
13            else:
14               icount = 1
15               dcount = 1
16            count = max(count,icount,dcount)
17        return count
18        