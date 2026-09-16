# Last updated: 9/16/2026, 12:00:07 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char in jewels:
            count += stones.count(char)
        return count
                