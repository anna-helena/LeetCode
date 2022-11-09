class Solution:
    def trap(self, height: List[int]) -> int:
        
        volume = 0
        start_height = 0
        start_idx = -1
        for idx,h in enumerate(height):
            if h >= start_height:
                for i in range(start_idx+1,idx):
                    volume += start_height - height[i]
                start_height = h
                start_idx = idx
        if start_idx != len(height)-1:
            start_idx_prev = start_idx
            start_height = 0
            start_idx = len(height)
            for idx in range(len(height)-1,start_idx_prev-1,-1):
                if height[idx] >= start_height:
                    for i in range(start_idx-1,idx,-1):
                        volume += start_height - height[i]
                    start_height = height[idx]
                    start_idx = idx
        return volume

            
        