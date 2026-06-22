class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        mini_price = prices[0]
        for i in range(len(prices)):
            mini_price = min(mini_price, prices[i])
            price = max(price, prices[i] - mini_price)
        return price
