/**
- Sort the array in ascending order 
- Have two pointers 
    - if the values of any 2 pointers is equal return true 
- iterate till the end of the array 
**/

class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums); 

        int i = 0; 
        int j = i+ 1; 

        for (i = 0; i < nums.length - 1; i++){
            if (nums[i] == nums[j]){
                return true;
            }
            j++;
        }

        return false; 
    }
}