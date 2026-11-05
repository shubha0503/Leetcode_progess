# Last updated: 11/5/2026, 10:40:53 PM
1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3
4        hashmap = {}
5        for i, num in enumerate(nums):
6            complement = target - num
7            if complement in hashmap:
8                return(hashmap[complement],i)
9            hashmap[num] = i
10        return []
11