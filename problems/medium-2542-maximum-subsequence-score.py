# this following code works

from operator import itemgetter
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []
        zipped = list(zip(nums1, nums2))        
        sortd = sorted(zipped, key=itemgetter(1), reverse=True)
        print(list(sortd))
        for a, b in sortd:
            prefixSum += a
            heapq.heappush(minHeap, a)
            if len(minHeap) == k:
                print(minHeap,b)                
                res = max(res, prefixSum * b)
                prefixSum -= heapq.heappop(minHeap)
        
        return res

# this code is reaching time limit for case 12/28
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
            how do I get the combination of indices form the given k
            once I have the combinations of length nk, calculate the sum and multiply with the nums2 counterpart, and take the max of them

            how to create k combinations?
          0          1      2       3
     1    2   3     2 3     3       0
    2 3   3         3
        '''


        def combinations(comb, rest, k, combs):
            if comb and len(comb) == k:
                combs.append(comb)
                return            
            for i,r in enumerate(rest):
                c = comb[:]
                c.append(r)
                combinations(c, rest[i+1:], k, combs)
        combs = []
        combinations([], list(range(len(nums1))), k, combs)

        scores = []
        for c in combs:
            totalSum = 0
            nums2Min = float('inf')
            for i in c:
                totalSum += nums1[i]
                nums2Min = min(nums2[i], nums2Min)            
            scores.append(totalSum * nums2Min)
        return max(scores)
            
