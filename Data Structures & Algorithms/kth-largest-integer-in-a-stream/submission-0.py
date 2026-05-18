import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums

        # have an initial stream of values nums -> need to get the kth largest from them
        # to do this we can a min heap and then pop until we have k elements left
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap) # does so in place

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) # to maintain heap property and ensure kth largest is at root

        return self.min_heap[0]
