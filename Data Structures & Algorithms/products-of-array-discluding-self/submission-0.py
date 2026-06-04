'''
- prefix, postfix values 

- the value that we need in the result array is: 
    - product of the elements before it (prefix values)
    - multiplied by the elements after it (postfix values)

Pseudocode: 

- init a result array 
- init the prefix as 1 

start prefix loop: 
    - every position in result array = prefix 
    - prefix value updates to prefix * nums[i]

start postfix loop: (iterate backwards): 
    - postfix = 1 
    - postfix value updates to postfix * nums[i]

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * (len(nums))

        prefix = 1 

        for i in range(len(nums)): 
            result[i] = prefix 
            prefix *= nums[i]

        postfix = 1 

        for i in range(len(nums) - 1, -1, -1): 
            result[i] *= postfix 
            postfix *= nums[i]

        return result 
        