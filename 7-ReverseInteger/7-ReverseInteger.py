# Last updated: 7/4/2026, 10:46:10 AM
class Solution:
    def reverse(self, x):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            rev = rev * 10 + digit
            
            if rev < INT_MIN or rev > INT_MAX:
                return 0
        
        return sign * rev