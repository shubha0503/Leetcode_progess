# Last updated: 8/8/2026, 10:52:23 AM
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums1 = sorted(set(nums))
        low = 0
        high = len(nums1)- 1
        while low <= high :
            mid = (low+high)//2
            if nums1[mid] == target:
                return  True
            elif nums1[mid] < target:
                low = mid +1
            else:
                high = mid -1
        return False