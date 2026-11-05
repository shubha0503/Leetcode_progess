# Last updated: 11/5/2026, 11:16:16 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = prices[0]
4        max_profit = 0
5        for price in prices:
6            min_price = min(min_price,price)
7            profit = price - min_price
8            if profit > max_profit:
9                max_profit = profit
10        return max_profit