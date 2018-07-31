class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curMax = curMin = res = nums[0]
        
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                curMax, curMin = curMin, curMax
            curMax = max(curMax * nums[i], nums[i])
            curMin = min(curMin * nums[i], nums[i])
            res = max(curMax, res)
            
        return res