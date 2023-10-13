class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        
        ans = 0
        buy, sell = prices[0], prices[0]
        
        for price in prices:
            if price < buy:
                buy, sell = price, price
            elif price > sell:
                sell = price
            ans = max(ans, sell - buy)
        
        return ans
