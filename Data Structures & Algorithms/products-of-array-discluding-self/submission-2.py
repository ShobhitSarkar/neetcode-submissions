"""
- initialize a result array with the same length as nums 
- set up prefix and postfix variables as 1 
- iterate through the array: 
    - assign nums[i] to prefix 
    - multiply prefix with the current nums number 
- iterate through the array once again (reverse)
    - multiply postfix with current number 
    - update postfix by multiplying it with the current number 

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        prefix = 1 
        postfix = 1 

        for i in range(len(nums)): 
            result[i] = prefix 
            prefix *= nums[i]

        for i in range(len(nums) - 1, - 1, -1): 
            result[i] *= postfix 
            postfix *= nums[i]

        return result


        