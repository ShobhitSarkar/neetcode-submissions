"""
- anagram - same characters, same frequency 

- iterate through first string: 
    - for each character in string - append to store, keep track of 
        frequency 

- iterate through the second string: 
    - if character doesn't exist - return false early 
    - if char exists, then reduce frequency 

- loop through hashmap, if the frequency is not 0, then return false 
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        store = {} 

        for char in s: 
            if char in store: 
                store[char] += 1 
            else: 
                store[char] = 1 

        for char in t: 
            if char not in store: 
                return False 
            else: 
                store[char] -= 1 

        for char in store: 
            if store[char] != 0: 
                return False 

        return True 
        