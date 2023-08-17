from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        lmax,rmax=height[left],height[right]
        water=0
        while left<right:
            lmax,rmax=max(lmax,height[left]),max(rmax,height[right])
            if lmax<=rmax:
                water+=lmax-height[left]
                left+=1
            else:
                water+=rmax-height[right]
                right-=1
        return water
    

if __name__ == "__main__":
    s = Solution()
    #output = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    output = s.trap([4,2,0,3,2,5])
    print(output)