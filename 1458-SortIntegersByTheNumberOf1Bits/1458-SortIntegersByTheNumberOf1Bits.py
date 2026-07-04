# Last updated: 7/4/2026, 10:43:45 AM
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (x.bit_count(), x))