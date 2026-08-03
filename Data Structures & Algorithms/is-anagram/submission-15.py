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
        