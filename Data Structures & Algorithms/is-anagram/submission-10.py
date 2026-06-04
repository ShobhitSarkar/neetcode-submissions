"""
- anagram: strings same, frequency same 

- iterate through first string, store char 
    and it's frequency 

- iterate through the second string: 
    - subtract the frequency 

- if the characters don't match - return false 
- if any frequency is anything other than 0 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        frequency = {} 

        for char in s: 
            if char in frequency: 
                frequency[char] += 1
            else: 
                frequency[char] = 1

        for char in t: 
            if char not in frequency: 
                return False 
            frequency[char] -= 1 

        for key in frequency: 
            if frequency[key] != 0: 
                return False 

        return True 
        