# Last updated: 8/19/2026, 1:35:51 AM
1class Solution:
2    def largestInteger(self, nums: List[int], k: int) -> int:
3        def f(k: int) -> int:
4            for i, x in enumerate(nums):
5                if i != k and x == nums[k]:
6                    return -1
7            return nums[k]
8
9        if k == 1:
10            cnt = Counter(nums)
11            return max((x for x, v in cnt.items() if v == 1), default=-1)
12        if k == len(nums):
13            return max(nums)
14        return max(f(0), f(len(nums) - 1))