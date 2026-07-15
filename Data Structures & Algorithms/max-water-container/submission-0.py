class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        maxwater=0 

        while left < right:
            # we need to find area 
            # and we need to keep the minimum one of the two lengths of bars
                   
                   #this gives the height we need       # this gives us width  
            area= min(heights[left],heights[right]) * (right - left)       
                                                    # width is difference of indices(x-axis)
            if maxwater < area:
                maxwater=area
            # now how do i mmove the pointers?
            # i need to shift the pointer whose value is smaller than the other
            # e.g we have min(2,7) now which pointer would you like to shift in order to get biggest area
            # obviously you would like to shift the smaller value because we want maximum area
            if heights[left] <= heights[right]:
                left+=1
            elif heights[left] >= heights[right]:
                right-=1
        return maxwater