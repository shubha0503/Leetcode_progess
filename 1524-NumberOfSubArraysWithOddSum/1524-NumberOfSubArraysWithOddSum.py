# Last updated: 11/25/2026, 7:55:58 PM
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        odd = 0
        even = 1

        prefix = 0
        ans = 0

        MOD = 10**9 + 7

        for num in arr:

            prefix += num

            if prefix % 2 == 1:
                ans += even
                odd += 1

            else:
                ans += odd
                even += 1

        return ans % MOD