"""
-- high level algorithm 

two big parts: 

- counting frequencies 
    - init a hashmap 
    - loop through the numbers 
        - if the number exists in hashmap, increase freq by 1 
        - if it doesn't, then add it to the hash with freq 1 
- manipulations to get the top k 
    - init an array 
    - store the pairings in this array as (frequency, element)
    - loop through the array, get the element value from the first k values 
    - build an array out of it and return 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        store = {} 

        ## counting frequencies 
        for num in nums: 
            if num in store: 
                store[num] += 1 
            else: 
                store[num] = 1 

        ## getting the top k frequencies 

        freq_array = []

        ## building the freq array with tuples 
        for f in store: 
            freq_array.append((store[f], f))

        freq_array.sort(reverse=True)

        result = [] 

        for i in range(k): 
            result.append(freq_array[i][1]) 

        return result 

    

        
        