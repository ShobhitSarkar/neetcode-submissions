'''
- we're keeping track of frequency - dict 

- iterate through the array & populate the dict: 
    - if number exists, then increase frequency by one 
    - if it doesn't exist, then add it with frequency 1 

----x we arrive with all elements with their frequencies 

----x we need to sort the frequencies and return the kth from the beginning 
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ## keep track of all the frequencies 
        frequencies = {} 

        ## calculate all the frequencies of the numbers 
        for num in nums: 
            if num in frequencies: 
                frequencies[num] += 1
            else: 
                frequencies[num] = 1

        ## get all of the frequencies and sort them 

        freq_array = [] 

        for freq in frequencies: 
            freq_array.append((frequencies[freq], freq))

        freq_array.sort(reverse=True) 

        result = [] 
        for i in range(k): 
            result.append(freq_array[i][1])
        
        return result
        