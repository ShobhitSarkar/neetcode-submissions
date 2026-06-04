'''
iterate through an array: 
    - store the seen numbers in a dict 
        - key: number itself, value: the index position 
    - if the current number in the array + seen number = target: 
        - then return the current index and the index of the other number
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} 

        for i, num in enumerate(nums): 
            complement = target - num
            if complement in seen: 
                return [seen[complement], i]
            else: 
                seen[num] = i
        