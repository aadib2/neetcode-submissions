class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # want to keep track of a left and right pointer, unique char occurrences, and length of window

        l = 0
        r = 0
        res = 0

        chars = {}

        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0) # update hashmap

            # if condition isn't valid (curr window size - num of most freq char > k) -> we need more than k replacements
            while (r-l+1) - max(chars.values()) >  k:
                chars[s[l]] -= 1 # update hashmap
                l+=1


            res = max(res, r-l+1) # compares max length to current size of window, if greater than update
        return res






        