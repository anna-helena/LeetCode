class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #trivial case: k = len(cardPoints) --> sum of all
        #tranform problem to find biggest sum window k in list of 2k array (k + 1 different sols)
        #at each window step, only calculate difference to --> 
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        base_sum = sum(cardPoints[:k])
        diff = 0
        max_diff = 0
        for step in range(1,k+1):
            diff = diff + cardPoints[-1*step] - cardPoints[k-1-1*(step-1)]
            if diff > max_diff:
                max_diff = diff
        return base_sum + max_diff