class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {} 

        for i in range(len(nums)): 
            store[nums[i]] = i 

        for i in range(len(nums)): 
            k = target - nums[i]

            if k in store and store[k] != i: 
                return [i , store[k]]

        return [] 
            
        