# Last updated: 8/8/2026, 10:51:14 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            count = 0
            for pile in piles:
                count += (pile + mid - 1) // mid

            if count <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans