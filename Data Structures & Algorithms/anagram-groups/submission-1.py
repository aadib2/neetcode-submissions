class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = dict() # could also use "{}"

        if len(strs) == 0:
            return [[""]]

        for word in strs:
            word_sorted = "".join(sorted(word))

            if word_sorted in hm:
                hm[word_sorted].append(word)
            else:
                hm[word_sorted] = [word]
        
        return list(hm.values())