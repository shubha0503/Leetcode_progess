# Last updated: 7/4/2026, 10:45:24 AM
class Solution(object):
    def mySqrt(self, x):
        
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right