class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {} 

        for i in range(len(nums)): 
            comp = target - nums[i]

            if comp in store and store[comp] != i: 
                return [min(store[comp],i), max(store[comp], i)]
            else: 
                store[nums[i]] = i 

        return [] 
        