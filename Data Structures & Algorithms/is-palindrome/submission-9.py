"""
- init a pointer on the left side 
- init a pointer on the right side 

- keep moving the pointers towards each other 
    - if at any point, the values don't line up then return false 

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(c for c in s.lower() if c.isalnum())
        
        left = 0 
        right = len(s) - 1  

        while left < right: 
            if s[left] != s[right]: 
                return False 
            left += 1 
            right -= 1 

        return True 
        