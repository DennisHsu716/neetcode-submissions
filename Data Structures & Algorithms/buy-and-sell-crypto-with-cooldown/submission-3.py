class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = float("-inf")
        rest = 0

        for i in range(len(prices)):
            old_hold = hold 
            old_sold = sold
            old_rest = rest 

            hold = max(old_hold, old_rest - prices[i])
            sold = prices[i] + old_hold
            rest = max(old_rest, old_sold)
        return max(sold, rest)