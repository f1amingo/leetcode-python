class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 0xff00ff
        max_profit = 0
        for price in prices:
            min_price = price if price < min_price else min_price
            max_profit = price - min_price if price - min_price > max_profit else max_profit
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
