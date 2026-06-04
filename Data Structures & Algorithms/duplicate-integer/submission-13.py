"""
- store: have hashmap of the stored elements 

- iterate through the array: 
    - if the element in store: 
        - return false 
    - if not in store: 
        - add in element 
- final return true 
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
        