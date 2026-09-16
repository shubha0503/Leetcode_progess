# Last updated: 9/16/2026, 12:00:09 PM
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Precomputed prime numbers up to 20
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        
        for num in range(left, right + 1):
            # Count set bits
            set_bits = bin(num).count('1')
            
            # Check if set bits count is prime
            if set_bits in prime_set:
                count += 1
                
        return count