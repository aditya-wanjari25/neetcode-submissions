class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left_buy = 0
        right_sell = 1

        while right_sell < len(prices):
            profit = prices[right_sell] - prices[left_buy]
            if profit > max_profit:
                max_profit = profit
            
            if prices[right_sell] < prices[left_buy]:
                left_buy = right_sell
            
            right_sell += 1
    
        return max_profit
            
        
