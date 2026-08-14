class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] 
        price = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            price = max(price, prices[i] - min_price)
        return price