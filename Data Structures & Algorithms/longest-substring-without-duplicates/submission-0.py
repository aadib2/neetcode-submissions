class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge cases
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        substr = set()

        l = 0
        max_len = 0

        # loop from r -> end of list
        for r in range(len(s)): # can also do while loop
            # check if str[r] in set, if so keep removing elements until we have a valid substr
            while s[r] in substr:
                # increment left pointer ('window) while this is true, also remove element from the set ('substring')
                substr.remove(s[l])
                l+=1
            # else
            substr.add(s[r])
            max_len = max(max_len, r - l + 1) # compare to size of current substring
        
        return max_len
        
        