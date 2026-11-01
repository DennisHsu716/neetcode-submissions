class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        max_price = 0

        for i in prices:
            price = min(price, i)
            max_price = max(max_price, i - price)
        return max_price