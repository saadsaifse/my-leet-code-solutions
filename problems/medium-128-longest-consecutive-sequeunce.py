from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        starts = []
        middles = []
        ends = []

        for n in uniqueNums:
            prev = n - 1
            nxt = n + 1

            if prev not in uniqueNums:
                starts.append(n)
            
            elif nxt not in uniqueNums:
                ends.append(n)

            else:
                middles.append(n)
        

        print(starts, middles, ends)

        starts= set(starts)
        middles= set(middles)
        ends= set(ends)

        counts = []
        c = 0
        j = 0
        for s in starts:
            c += 1
            j = s + 1
            while j in middles:
                c+=1
                j += 1
            if c >= 1 and len(ends) > 0:
                c += 1            
            counts.append(c)        
            c = 0

        return max(counts, default = 0)
       
    
if __name__ == "__main__":
    s = Solution()
    output = s.longestConsecutive([100,4,200,1,3,2])
    #output = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
    #output = s.longestConsecutive([5,100,1000,1000000, 0,101,102, -1,103,-5])
    print(output)