class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 ,1
        maxProfit = 0
        while l < r and r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit



        # l , r = 0, 1
        # max_profit = 0
        # while r < len(prices) :
        #     print(l , r, max_profit)
        #     if prices[r] > prices[l]  :
        #         max_profit = max(max_profit, prices[r] - prices[l])   
        #     else:
        #         l = r
        #     r = r + 1
        # return max_profit
        