/**
- first of all store all the characters of the string in an array 
- Check if length is ==, then proceed, else false 
- Sort both of these arrays: 
    - and do equals comparison 
**/

class Solution {
    public boolean isAnagram(String s, String t) {

        char[] sChars = new char[s.length()]; 
        char[] tChars = new char[t.length()]; 

        for (int i = 0; i < s.length();i++){
            sChars[i] = s.charAt(i);
        }

        for (int i = 0; i < t.length(); i++){
            tChars[i] = t.charAt(i);
        }

        if (sChars.length != tChars.length){
            return false;
        }

        Arrays.sort(sChars); 
        Arrays.sort(tChars); 

        return Arrays.equals(sChars, tChars);

    }
}
