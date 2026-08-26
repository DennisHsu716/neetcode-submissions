class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        price = 0 
        for i in prices:
            min_price = min(min_price, i)
            price = max(price, i - min_price)
        return price