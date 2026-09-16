# Last updated: 9/16/2026, 11:59:37 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low+high)//2
            k = 0
            for pile in piles:
                k += ceil(pile/mid)
            if k <= h:
                high = mid -1
            else:
                low = mid+1
        return low  