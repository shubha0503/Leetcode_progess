# Last updated: 9/16/2026, 11:58:30 AM
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (x.bit_count(), x))