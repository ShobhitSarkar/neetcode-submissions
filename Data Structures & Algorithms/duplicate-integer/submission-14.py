"""
tracking seen elements - store 

iterate through the elements of the array: 
    - on every element:
        - if element exists in hashmap -> return true 
        - if doesn't -> add it to the hashmap 

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
        