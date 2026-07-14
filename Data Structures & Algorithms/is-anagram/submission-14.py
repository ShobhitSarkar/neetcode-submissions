"""
anagram: same characters and same frequency 

-- high level algorithm: 

- init a hashmap to store the characters & the frequency 
- iterate through the first string: 
    - if that char is in hashmap, then increase it's frequency 
    - if it is not, add it to hashmap with frequency 1 
- iterate through the second string: 
    - if the character is not in hashmap, then return false 
    - if the character is in the hashmap, then subtract 1 from it's freq
- loop through the hashap: 
    - if the frequency on any of the characters is not 0, return false 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        store = {} 

        for ch in s: 
            if ch in store: 
                store[ch] += 1 
            else: 
                store[ch] = 1 

        for ch in t: 
            if ch not in store: 
                return False
            store[ch] -= 1 

        for ch in store: 
            if store[ch] != 0: 
                return False 

        return True

        
        