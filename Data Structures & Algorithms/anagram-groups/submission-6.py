"""
-- high level algorithm

- hashmap / default dict for grouping the anagrams 
- key? 
    - sorted version of each of the anagrams is going to be same 
    - same characters + same character frequency 

- init a default dict 
- start iterating through the string: 
    - sort the given string (key)
    - if the key is within the hashmap: 
        - add this word to the list for that key 
    - if it is not: 
        - create a new item in the default dict
        - add this word to it 

(helper) sorting a word: 

- convert the word and put it into an array 
- sort the array 
- convert back into word and then return 
- O(n log n)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = defaultdict(list) 

        for string in strs: 
            key = self.generate_key(string)

            store[key].append(string)

        result = [] 

        for word in store: 
            result.append(store[word])
        
        return result


    def generate_key(self, word: str) -> str: 
        """
        helper method to sort a given word 
        """

        return "".join(sorted(word))



        