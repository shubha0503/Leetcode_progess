# Last updated: 7/16/2026, 3:30:26 AM
from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd = 0
        sumeven = 0
        for i in range(1,(n*2)+1):
            if i % 2 == 0:
                sumeven += i
            else:
                sumodd += i
        
        return gcd(sumodd,sumeven)