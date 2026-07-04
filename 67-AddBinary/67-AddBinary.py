# Last updated: 7/4/2026, 10:45:26 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Iterate from right to left
        while i >= 0 or j >= 0 or carry:
            # Add carry and values from a and b if pointers are in bounds
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
                
            # Current digit is carry % 2, new carry is carry // 2
            ans.append(str(carry % 2))
            carry //= 2
            
        # Reverse and join the list to get the final string
        return "".join(ans[::-1])
