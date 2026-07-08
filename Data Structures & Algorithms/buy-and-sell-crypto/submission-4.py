class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        price = 0
        for i in prices:
            mini = min(mini, i)
            price = max(price, i - mini)
        return price