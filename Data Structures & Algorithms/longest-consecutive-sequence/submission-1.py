'''
- from the sample test cases - we don't care about duplicates 
and are only concerned about unique numbers 
    - points me towards a set 

- how does sequence begin: 
    - if num - 1 doesn't exist in set 

- once num is achieved, 
    - the length of the sequence grows as long as num + length numbers 
        are there in the set. 
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ## init a set of numbers 
        num_set = set(nums)

        ## init var to track longest sequence 
        longest = 0 

        for num in num_set: ## iterate through all the nums in array 
            if (num - 1) not in num_set: 
                length = 1
                while (num + length) in num_set: ## this is a O(1) operation actually
                    length += 1
                longest = max(length, longest)
        
        return longest
        