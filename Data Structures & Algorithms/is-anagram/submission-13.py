"""
- anagrams = same characters, same frequency 

- init a hashmap
- start iterating through the first string 
    - if the character exists in the hashmap, then increase the frequency by one 
    - if it doesn't exist, then add it to the hashmap with frequency 1 
- iterate through the second string: 
    - if the character doesn't exist in the hashmap, return false 
    - if it does exist, then reduce frequency by 1 
- iterate through the hashmap: 
    - if any of the values are not 0, return false 
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
            else: 
                store[ch] -= 1 

        for ch in store: 
            if store[ch] != 0: 
                return False 

        return True 
        