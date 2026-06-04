/**
Solution : 

- get rid of any spaces and make all of the data lower case 
- have two pointers at the begining and end of the string. 
- check if the character at both pointers is equal 
**/

class Solution {
    public boolean isPalindrome(String s) {

        String cleanedS = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", ""); 


        int left = 0; 
        int right = cleanedS.length() -1; 

        while (left < right){
            if (cleanedS.charAt(left) != cleanedS.charAt(right)){
                return false;
            }
            left ++; 
            right --; 
        }

        return true;
        
    }
}
