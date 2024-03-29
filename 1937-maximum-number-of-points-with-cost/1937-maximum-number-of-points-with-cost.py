class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        a=len(points[0])
        b=len(points)
        for i in range(b-1):
            for j in range(1,a):
                points[i][j]=max(points[i][j], points[i][j - 1] - 1)
            for j in range(a-2,-1,-1):
                points[i][j]=max(points[i][j], points[i][j + 1] - 1)
            for j in range(a):
                points[i+1][j]+=points[i][j]
        
        return max(points[b-1])
