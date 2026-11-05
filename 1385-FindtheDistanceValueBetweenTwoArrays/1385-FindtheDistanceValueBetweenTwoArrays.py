# Last updated: 11/5/2026, 10:59:21 PM
1class Solution:
2    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
3        count = 0
4        for i in range(len(arr1)): 
5            valid = True   
6            for j in range(len(arr2)):
7                if abs(arr1[i] - arr2[j]) <= d:
8                    valid = False
9            if valid:
10                count += 1
11        return count
12        