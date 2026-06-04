"""
- init a hashmap to keep track of seen elements 
- start iterating through the array: 
    - if the element doesn't exist in the hashmap, then add it to it 
    - if the element exists in the hashmap, then return true 
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        store = {} 

        for i in range(len(nums)): 
            if nums[i] in store: 
                return True 
            else: 
                store[nums[i]] = 1 

        return False
        