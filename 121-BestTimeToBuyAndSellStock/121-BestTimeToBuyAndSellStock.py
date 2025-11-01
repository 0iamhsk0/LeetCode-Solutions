# Last updated: 11/1/2025, 9:34:41 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < bp:
                bp = price

            profit = max(profit, price - bp)

        return profit       