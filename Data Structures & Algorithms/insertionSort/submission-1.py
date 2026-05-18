# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []

        if len(pairs) == 0: # base case
            return states


        states.append(pairs.copy()) # add initial list

        # insertion sort logic
        for i in range(1, len(pairs)):
            j = i - 1
            curr = pairs[i]

            while curr.key < pairs[j].key and j >= 0:
                # move pair over
                pairs[j+1] = pairs[j]
                # update j
                j-=1
            
            pairs[j+1] = curr
            # add current state of pairs to the states
            states.append(pairs.copy())
        
        return states
