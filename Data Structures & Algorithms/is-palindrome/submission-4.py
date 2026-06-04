'''
- add the characters to an array 
- one pointer on the left, one pointer on the right 
    - match the elements on the two pointers 
    - if they're equal, then continue
    - if not, then return false 

caveats: 
    - remove spaces 
    - remove special characters 
    - make the solution case insensitive 
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_str = ''

        for char in s: 
            if char.isalnum(): 
                cleaned_str += char.lower()

        left = 0 
        right = len(cleaned_str) - 1 

        while left < right: 
            if cleaned_str[left] == cleaned_str[right]: 
                left += 1 
                right -= 1
            else: 
                return False 

        return True

        