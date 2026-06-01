import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap)==len(self.max_heap) and len(self.min_heap)==0:
            heapq.heappush(self.min_heap, num)
            return
        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap,-1*num)
        
        while abs(len(self.min_heap)-len(self.max_heap))>1:
            if len(self.min_heap) > len(self.max_heap):
                smallest = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,-1*smallest)
            else:
                largest = -1*heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,largest)


        

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return   self.min_heap[0]
        elif len(self.min_heap) == len(self.max_heap):
            return   (self.min_heap[0] -   self.max_heap[0])/2
        else:
             return -1* self.max_heap[0]
        
        
        