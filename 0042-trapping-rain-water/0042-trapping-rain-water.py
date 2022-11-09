class Solution:
    def trap(self, height: List[int]) -> int:
        
        volume = 0
        start_height = 0
        start_idx = -1
        for idx,h in enumerate(height):
            if h >= start_height:
                print(start_height,h)
                for i in range(start_idx+1,idx):
                    print(i,start_height - height[i])
                    volume += start_height - height[i]
                start_height = h
                start_idx = idx
                print('----')
        print('start_idx',start_idx)
        print(len(height)-1)
        if start_idx != len(height)-1:
            print('test',len(height)-1,start_idx-1)
            start_idx_prev = start_idx
            start_height = 0
            start_idx = len(height)
            for idx in range(len(height)-1,start_idx_prev-1,-1):
                print(height[idx],idx)
                if height[idx] >= start_height:
                    print(start_height,height[idx],idx)
                    print('loop')
                    print(start_idx,idx)
                    for i in range(start_idx-1,idx,-1):
                        print(i,start_height - height[i])
                        volume += start_height - height[i]
                    start_height = height[idx]
                    start_idx = idx
                    print('----')
        return volume

            
        