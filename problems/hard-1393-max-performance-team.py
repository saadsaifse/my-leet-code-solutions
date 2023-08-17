import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        res, speedSum, minHeap = 0, 0, []
        
        for ef, sp in sorted(zip(efficiency, speed), reverse=True):
            speedSum += sp
            heapq.heappush(minHeap, sp)
            res = max(res, speedSum * ef)
            if len(minHeap) == k:
                speedSum -= heapq.heappop(minHeap)
        
        return res % (10**9 + 7)