# Last updated: 7/8/2026, 4:29:48 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        val = []
        n = len(accounts)
        m = len(accounts[0])
        
        for i in range(n):
            sum = 0
            for j in range(m):
                
                sum += accounts[i][j]
            val.append(sum)
        ans = max(val)
        return ans

        

        