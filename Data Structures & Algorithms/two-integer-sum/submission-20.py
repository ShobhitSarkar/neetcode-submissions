"""
- init a hashmap
- start by iterating through the array: 
    - calculate the complement to the number 
    - if the complement exists, then return the current index and index 
        stored in the hashmap 
    - if the complement doesn't exist, then add the current number with 
        it's index in the hashmap 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {} 

        for i in range(len(nums)): 

            complement = target - nums[i]

            if complement in store: 
                return [store[complement], i]
            else: 
                store[nums[i]] = i 

        return [] 