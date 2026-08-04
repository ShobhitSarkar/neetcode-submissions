"""
step 1: counting frequency 
    - init a hashmap 
    - loop through the nums, increase frequency by one 
        (key, value) = (number, frequency)

step 2: arranging in descending order 
    - init a an array with (frequency, number) tuples 
    - sort the array (O(nlogn))
    - then return frequency of the first k elements of the sorted 
        array 
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ## frequency counting 

        freq = {} 

        for num in nums: 
            if num in freq: 
                freq[num] += 1 
            else: 
                freq[num] = 1 

        ## arranging frequencies 

        freq_array = [] 

        for num in freq: 
            freq_array.append((freq[num], num))
        
        freq_array.sort(reverse=True)

        result = [] 

        for i in range(k): 
            result.append(freq_array[i][1])

        return result
            
        
        