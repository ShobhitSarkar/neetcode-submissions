'''
- same characters, same frequencies 

- take the first string: 
    - add it in the hashmap with frequency 

- take the second string: (break according to character)
    - if the character doesn't exist: 
        - return false 
    - if it does, reduce the frequency by one 

- loop through the seen: 
    - if frequency anything more than 0: 
        - return False 
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        frequencies = {} 

        for char in s: 
            if char in frequencies: 
                frequencies[char] += 1
            else: 
                frequencies[char] = 1
        
        for char in t: 
            if char not in frequencies: 
                return False 
            else: 
                frequencies[char] -=1 
        
        for char in frequencies: 
            if frequencies[char] > 0: 
                return False 

        return True 
        