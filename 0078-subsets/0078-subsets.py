class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for num in nums:
            temp = []
            for re in res:
                temp.append(re+[num])
            res += temp
        return res
            
        