class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base cases
        if len(s1) > len(s2):
            return False
        
        if s1 == '': # if s1 is empty, it is automatically true
            return True


        # sliding window

        # keep track of an array of counts / frequencies
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False





            # if char isn't in dict
              # update left pointer & dictionary



        # brute force is to sort both strings

        # then compare each substring in s2

        # s1 = sort(s1)
        # s2 = sort(s2)


        # for i in range(len(s2)):
        #     curr_s = s2[i: i + len(s1)]


        #     if curr_s == s1:
        #         return True
        
        # return False