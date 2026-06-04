"""
- if k = 2, second most frequent elements in the array 
    - first most frequeny, second most frequent 

- store for the frequencies 
- iterate through the array: 
    - calculate the frequencies 
- get all the frequencies - sort in descending order 
- get k, ie kth element from the beginning 
- then iterate through the frequencies, get all the frequencies greater 
    than k
- get the values of the numbers 

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {} 

        for num in nums: 
            if num in frequencies: 
                frequencies[num] += 1 
            else: 
                frequencies[num] = 1 

        freq_array = [] 
        
        for key in frequencies: 
            freq_array.append(frequencies[key])

        freq_array.sort(reverse = True)
        
        limit = freq_array[:k]

        min_freq = limit[-1]
        result = [] 
        for element in frequencies: 
            if frequencies[element] >= min_freq: 
                result.append(element)

        return result 

        