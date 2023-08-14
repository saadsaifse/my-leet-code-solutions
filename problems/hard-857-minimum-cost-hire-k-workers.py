import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res, qualitySum, maxHeap = float('inf'), 0, []
        zipped = zip(wage, quality)        
        wageQualityRatio = [(w / q, q) for w, q in zip(wage, quality)]        
        sortedWageQualityRatio = sorted(wageQualityRatio)        
        for ration, q in sortedWageQualityRatio:
            qualitySum += q
            heapq.heappush(maxHeap, -q)
            if len(maxHeap) == k:
                res = min(res, qualitySum * ration)
                qualitySum -= -heapq.heappop(maxHeap)
        
        return res