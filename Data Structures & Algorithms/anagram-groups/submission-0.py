class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # create dictionary of groups


        for word in strs: # O(m) where m is number of strings in strs
            sorted_word = "".join(sorted(word)) # should be O(n log n) where n is length of string

            if sorted_word in groups:
                groups[sorted_word].append(word) # if it is an anagram then add it to the existing group
            else:
                # if it is a new word then add it as key-value pair to dict
                groups[sorted_word] = [word]
        
        return list(groups.values())


            


            

