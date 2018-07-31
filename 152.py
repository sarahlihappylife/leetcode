class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curMax = curMin = maxProduct = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                curMax, curMin = curMin, curMax
            curMax = max(curMax * num, num)
            curMin = min(curMin * num, num)
            maxProduct = max(curMax, maxProduct)
            
        return maxProduct