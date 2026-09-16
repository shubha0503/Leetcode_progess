# Last updated: 9/16/2026, 11:57:26 AM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        
        for i in range(len(accounts)):
            amt = 0
            for j in range(len(accounts[i])):
                amt += accounts[i][j]
            wealth.append(amt)
        return max(wealth)
        
            

            
         