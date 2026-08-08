# Last updated: 8/8/2026, 10:51:13 AM
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            return max(piles[i] - dfs(i + 1, j), piles[j] - dfs(i, j - 1))

        return dfs(0, len(piles) - 1) > 0