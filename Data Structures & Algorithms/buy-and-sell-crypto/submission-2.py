"""
-- high level algorithm: 
    - init some variables: 
        - buy - set it at the beginning of the array 
        - max profit - keep track of the maximum profit 
    - move sell pointer through the array: 
        - if the value[buy] > sell: 
            - then update the max profit 
        - if it is not, then move the buy pointer to sell
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0 
        max_profit = 0 

        for sell in range(1, len(prices)): 
            if prices[sell] > prices[buy]: 
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else: 
                buy = sell 

        return max_profit 
        