"""
anagram: 
    - same characters 
    - same frequency of the characters 

- create dict to store the anagrams (default dict)
- need a key for each anagram - sorted version of the word 
    - if the sorted version of the word = key, add it to hashmap     

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = defaultdict(list)

        for string in strs: 
            key = tuple(sorted(string))
            store[key].append(string)

        ## creating the result 
        result = [] 

        for key in store: 
           result.append(store[key])
        
        return result

    

    
        