"""
-- high level algorithm 

- init a hashmap 
    - add all of the numbers with the corresponding index value 
        to the hashmap 
- start iterating through the array: 
    - for every number, calculate the complement to the number 
    - if it exists in hashmap, return current index & index of num in hashmap 
    - if it doesn't exist, then add the current number to the hashmap with

caveats: 
- while comparing, make sure it's not current index you're on 
- when generating result, make sure smaller index first 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {} 

        for i in range(len(nums)): 
            store[nums[i]] = i 

        for i in range(len(nums)): 
            complement = target - nums[i]
            
            if complement in store and store[complement] != i: 
                return [store[complement], i] if store[complement] < i else [i, store[complement]]

        
        return [] 
        