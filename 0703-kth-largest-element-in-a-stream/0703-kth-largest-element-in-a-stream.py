class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums #make the list of nums a min heap
        heapq.heapify(self.heap)  #turns the list into a valid min heap
        
        while len(self.heap) > k: #no point in it being longer than k since u will never need a value larger than k
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) #push the value into the min heap
        if len(self.heap) > self.k: #if the push made the len larger than k remove the last value
            heapq.heappop(self.heap)
        return self.heap[0] #return the 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)