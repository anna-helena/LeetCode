class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height)-1
        curr_max = 0
        while i<j:
            curr_max = max(curr_max,min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i_prev = i
                while (i<j) & (height[i_prev]>=height[i]):
                    i += 1
            else:
                j_prev = j
                while (i<j) & (height[j_prev]>=height[j]):
                    j -= 1
        return curr_max
                
            
        