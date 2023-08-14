from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        mergedIntervals = []

        lastMaxValue = intervals[0][-1]
        mergeStartIndex = 0
        mergeEndIndex = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= lastMaxValue:
                mergeEndIndex = i                
            else: 
                if mergeStartIndex != mergeEndIndex:
                    mergedIntervals.append([intervals[mergeStartIndex][0],lastMaxValue])                    
                else:
                    mergedIntervals.append(intervals[mergeStartIndex])
                mergeStartIndex = mergeEndIndex = i
            lastMaxValue = max(lastMaxValue, intervals[i][1])

        if mergeStartIndex != mergeEndIndex:
            mergedIntervals.append([intervals[mergeStartIndex][0], lastMaxValue])                    
        else:
            mergedIntervals.append(intervals[mergeStartIndex])
        return mergedIntervals
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18],[1, 4]]))
    print(sol.merge([[1,4],[4,5]]))

