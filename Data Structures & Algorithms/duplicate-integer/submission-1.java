/**
Possible Solution: 
- sort the array 
- have a nested loop which looks if any two adjacent elements are the same 
**/

class Solution {
    public boolean hasDuplicate(int[] nums) {

        for (int i = 0; i < nums.length -1; i++){
            for (int j = i+1; j < nums.length; j++){
                if (nums[i] == nums[j]){
                    return true;
                }
            }
        }

        return false;
 
    }
}
