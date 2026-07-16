"""
-- given: 
    - array sorted in ascending order

-- high level algorithm: 

- init two pointers: left and right 
    - left: first index of the array 
    - right: last index of the array 

- calculate the sum of the two numbers 
    - if the sum is greater than target: 
        - move the right pointer backwards 
    - if the sum is less than the target: 
        - move the left pointer forwards 
    - if it equals the target: 
        - return the values of the two pointers 


"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 
        right = len(numbers) - 1 

        while left < right: 
            sum = numbers[left] + numbers[right]

            if sum == target: 
                return [left + 1, right + 1] ## 1 indexed
            elif sum > target: 
                right -= 1 
            else: 
                left += 1 

        return [] 
        