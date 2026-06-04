'''
need to keep track of elements 

- init a dictionary 
- iterate through the array: 
    - if element exists in hash map - return true 
    - if it doesn't, add it to the hash map 

- make sure to start by adding the first element in the dict 

edge cases: 
    - array of length 0 
    - array of length 1 
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0: 
            return False 

        if len(nums) == 1: 
            return False 

        seen = {} 
        seen[nums[0]] = None 

        for i in range(1, len(nums)): 
            if nums[i] in seen: 
                return True 
            else: 
                seen[nums[i]] = None

        return False


        