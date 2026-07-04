# Last updated: 7/4/2026, 10:43:32 AM
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left (ignore first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                # odd → +1 then divide
                steps += 2
                carry = 1
            else:
                # even → just divide
                steps += 1
        
        return steps + carry