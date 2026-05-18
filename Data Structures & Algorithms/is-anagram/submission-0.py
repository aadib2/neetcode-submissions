class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str_counts = {}
        for c in t:
            # add unique characters and their corresponding counts to dict
            str_counts[c] = str_counts.get(c, 0) + 1

        for c in s:
            if c in str_counts and str_counts[c] > 0:
                str_counts[c]-= 1
            else:
                return False
        return True
        

        


        