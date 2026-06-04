/**
Have two pointers: 
    - one which tracks when to buy 
    - one which tracks when to sell 
- For each and every time the buy pointer moves: 
    - Check the difference between the buy and sell price 
    - Update the difference to be the maximum 
- return the difference  
***/

class Solution {
    public int maxProfit(int[] prices) {

        int diff = 0;
        int counter = 0; 


        for (int i = 0; i < prices.length - 1; i ++){
            for (int j = i+1; j < prices.length; j++){
               counter = prices[i] - prices[j];
               if (counter < diff){
                diff = counter;
               }
                
            }
        }

        return -diff;
        
    }
}
