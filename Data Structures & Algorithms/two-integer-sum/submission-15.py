"""
- store all elements in hashmap 
- for every num, calculate compliment: 
    - if the compliment exists in the hashmap, 
        then return the current index & value of hashmap 
- while populating hashmap, key=number, value = index 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {} 

        for i in range(len(nums)): 
            store[nums[i]] = i 

        for i in range(len(nums)): 
            complement = target - nums[i]
            if complement in store and store[complement] != i: 
                return [i, store[complement]]

        return [] 
        