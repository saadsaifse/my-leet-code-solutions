import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.rangeStart = 1
        self.addedBack = set()                     

    def popSmallest(self) -> int:
        previousRangeStart = self.rangeStart
        nums = list(self.addedBack)
        nums.append(previousRangeStart)
        heapq.heapify(nums)       
        popped = heapq.heappop(nums)
        if popped in self.addedBack:
            self.addedBack.remove(popped)
        else:
            self.rangeStart += 1
        return popped


    def addBack(self, num: int) -> None:
        if num >= self.rangeStart:
            return
        self.addedBack.add(num)       
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)