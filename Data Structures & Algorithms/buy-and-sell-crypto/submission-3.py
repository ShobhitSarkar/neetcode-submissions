"""
-- high level algorithm:

    - init a couple of variables: 
        - buy - pointer to first element in the array 
        - max_profit - counter variable to keep track of maximum profit 
    - start iterating from the second element on: 
        - if the prices[sell] > prices[buy]: 
            - update the max profit variable
        - if not, move buy up to sell 

    - return the max profit 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 
        buy = 0 

        for sell in range(1, len(prices)): 
            if prices[sell] > prices[buy]: 
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else: 
                buy = sell 

        return max_profit
        