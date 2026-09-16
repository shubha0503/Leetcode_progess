# Last updated: 9/16/2026, 11:59:21 AM

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            days1 = 1
            load = 0

            for i in range(len(weights)):
                if load + weights[i] > mid:
                    days1 += 1
                    load = 0

                load += weights[i]

            if days1 <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low

