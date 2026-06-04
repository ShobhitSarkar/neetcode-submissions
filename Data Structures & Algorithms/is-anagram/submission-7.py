'''
keep track of: 
    - characters 
    - their frequency 

- init a hashmap 
- iterate through first string: 
    - if characters exists in the hashmap: 
        - increase frequency 

    - if it doesn't 
        then add it to hashmap with frequency = 1 

- iterate through the second string: 
    - if the character doesn't exist in the hashmap: 
        - return false 
    - if it does: 
        then reduce frequency by 1 
    
- iterate through hashmap and then if the frequency is not 0: 
    - return false 
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False
        
        seen = {} 

        for char in s: 
            if char in seen: 
                seen[char] += 1 
            else: 
                seen[char] = 1 

        for char in t: 
            if char not in seen: 
                return False 
            else: 
                seen[char] -= 1

        for char in seen: 
            if seen[char] != 0: 
                return False 

        return True

        