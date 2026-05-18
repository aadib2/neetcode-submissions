from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # other ways to solve this as well -> using a hashmap + heap -> pop k values off heap
        highest = Counter(nums)     
        return sorted(highest, 
        key= lambda x: highest[x], reverse=True)[:k]