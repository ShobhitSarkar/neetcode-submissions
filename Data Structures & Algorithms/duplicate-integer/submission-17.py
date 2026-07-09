"""
- init a hashmap 
- iterate through the array: 
    - if the hashmap has the number: 
        - return false 
    - if it doesn't have it: 
        - add the number to the hashmap 
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        store = {} 

        for num in nums: 
            if num in store: 
                return True
            else: 
                store[num] = True 

        return False
        