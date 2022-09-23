class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        #no ones --> ok
        #entire rows and cols --> ok
        set_1 = set()
        set_0 = set()
        for i,val in enumerate(grid[0]):
            if val == 0:
                set_0.add(i)
            else:
                set_1.add(i)
        for row_idx in range(1,len(grid)):
            row = grid[row_idx]
            set_0_temp = set()
            set_1_temP = set()
            for i,val in enumerate(row):
                if val == 0:
                    set_0_temp.add(i)
                else:
                    set_1_temP.add(i)
            if((set_0_temp != set_0) & (set_0_temp != set_1)):
                return False
        return True
                