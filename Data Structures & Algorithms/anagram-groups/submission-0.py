'''
way to check for anagram: 
- if the length of strings is different -> not in anagram 
- store the frequencies of each character for first string 
- while iterating through the second string, subtract the frequency 
    - if frequency is < 0 for all characters, then anagram 

main issue here: 
    - how do you get two terms that might be anagrams together 

checking the anagram is easy -> we are just counting frequencies 

hashmap approach: 
    - if the word is an anagram -> each sorted word will be the same 
    - use this as a key in the hashmap 
    - init the hashmap as default dict, where the the value is a list 
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = defaultdict(list)

        for s in strs: 
            sorted_s = ''.join(sorted(s))
            store[sorted_s].append(s)

        return list(store.values())

        
        
        