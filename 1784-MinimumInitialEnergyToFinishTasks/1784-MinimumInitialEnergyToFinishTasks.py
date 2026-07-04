# Last updated: 7/4/2026, 10:43:12 AM
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = cur = 0
        for a, m in sorted(tasks, key=lambda x: x[0] - x[1]):
            if cur < m:
                ans += m - cur
                cur = m
            cur -= a
        return ans