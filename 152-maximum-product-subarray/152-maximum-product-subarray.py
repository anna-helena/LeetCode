class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_prod_k = nums
        max_min = 1
        if nums[0] < 0:
            max_min = nums[0]
        for i,val in enumerate(nums[1:]):
            i += 1
            #print(i, max_min, max_prod_k)
            if(val == 0):
                max_min = 1
            elif(val>0):
                if(max_prod_k[i-1]>0):
                    max_prod_k[i] = max_prod_k[i-1]*val
                    if(max_min<0):
                        max_min*=val
                elif(max_prod_k[i-1]<0):
                    max_min *=val            
            elif(val<0):
                max_prod_k[i] = max_min*val
                if(max_prod_k[i-1]>0):
                    max_min = val*max_prod_k[i-1]
                elif(max_prod_k[i-1]<=0):
                    max_min = val
                
        return(max(max_prod_k))
    
            
            
            