# Last updated: 9/16/2026, 11:59:41 AM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high)//2
            if arr[mid] > arr[mid +  1]:
                high = mid 
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
        return low
        