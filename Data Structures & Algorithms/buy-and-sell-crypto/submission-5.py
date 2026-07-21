class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        mini = prices[0]
        for i in prices:
            mini = min(mini, i)
            price = max(price, i - mini)
        return price