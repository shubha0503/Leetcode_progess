# Last updated: 7/4/2026, 10:46:09 AM
class Solution:
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            
            # 4. Clamp early
            if sign * num <= INT_MIN:
                return INT_MIN
            if sign * num >= INT_MAX:
                return INT_MAX
            
            i += 1
        
        return sign * num