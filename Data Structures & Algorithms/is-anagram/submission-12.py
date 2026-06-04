"""
anagram - same characters, same frequency of each character 

algo: 
    - iterate through the first string: 
        - keep track of each of the characters & their frequencies 
    - iterate through the second string: 
        - if there's a character that's not in store -> return false 
        - if character in store - minus one frequency 
    - loop through all of the elements in the store 
        - if the frequency is not 0, return false 

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