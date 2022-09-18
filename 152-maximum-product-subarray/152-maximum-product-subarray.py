class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_prod_k = nums[0]
        max_min = 1
        result = max_prod_k
        if nums[0] < 0:
            max_min = nums[0]
        for i,val in enumerate(nums[1:]):
            i += 1
            #print(i, max_min, max_prod_k)
            temp = val
            if(val == 0):
                max_min = 1
            elif(val>0):
                if(max_prod_k>0):
                    temp = max_prod_k*val
                    if(max_min<0):
                        max_min*=val
                elif(max_prod_k<0):
                    max_min *=val            
            elif(val<0):
                temp = max_min*val
                if(max_prod_k>0):
                    max_min = val*max_prod_k
                elif(max_prod_k<=0):
                    max_min = val
            result = max(result,temp)
            max_prod_k = temp
            #max_prod_k[i] = max(val, max_prod_k[i-1]*val, max_min*val)
            #max_min = 
        return result
    
            
            
            