# Last updated: 7/29/2026, 10:46:57 AM
1class Solution:
2    def peakIndexInMountainArray(self, arr: List[int]) -> int:
3        low = 0
4        high = len(arr) - 1
5        while low < high:
6            mid = (low + high)//2
7            if arr[mid] > arr[mid +  1]:
8                high = mid 
9            elif arr[mid] < arr[mid + 1]:
10                low = mid + 1
11        return low
12        