'''
we need to keep track of the characters that we've seen -> dict 

iterate through the strings: 
    for the first string: 
        - add all the characters to the dict as the key 

    for the second string: 
        keep making the assertion that the current character in dict 
        if the current char doesn't exist in dict -> return false

    problem -> duplicates 
        - change the value of the key to be counter variable 
        - additional condition: 
            - if the character is in the hashmap, reduce the frequency by 1 

        - at every iteration, do a check if the frequency is 0, if it is, then it's fale 


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
            seen[char] -= 1
            if seen[char] < 0: 
                return False
                
        
        return True 
        