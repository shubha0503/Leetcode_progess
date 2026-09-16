# Last updated: 9/16/2026, 11:57:37 AM
class Solution:
    def minimumDeletions(self, s):
        count_b = 0
        deletions = 0

        for ch in s:
            if ch == 'b':
                count_b += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, count_b)

        return deletions
