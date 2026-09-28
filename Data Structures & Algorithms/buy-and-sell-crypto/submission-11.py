class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini_price = prices[0]
        price = 0

        for i in prices:
            mini_price = min(mini_price, i)
            price = max(price, i - mini_price)
        return price