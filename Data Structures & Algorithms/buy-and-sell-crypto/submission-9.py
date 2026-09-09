class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini_prices = prices[0] 
        price = 0 

        for i in prices:
            mini_prices = min(mini_prices, i)
            price = max(price, i - mini_prices)
        return price