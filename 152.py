class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # curMax = curMin = res = nums[0]
        
        # for i in xrange(1, len(nums)):
        #     if nums[i] < 0:
        #         curMax, curMin = curMin, curMax
        #     curMax = max(curMax * nums[i], nums[i])
        #     curMin = min(curMin * nums[i], nums[i])
        #     res = max(curMax, res)
            
        # return res


        curMax = curMin = res = nums[0]
        maxIdx = minIdx = 0
        resIdx = (0, 0)
        
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                curMax, curMin = curMin, curMax
                maxIdx, minIdx = minIdx, maxIdx

            if nums[i] > curMax * nums[i]:
                maxIdx = i
                curMax = nums[i]
            else:
                curMax = curMax * nums[i]

            if nums[i] < curMin * nums[i]:
                minIdx = i
                curMin = nums[i]
            else:
                curMin = curMin * nums[i]

            if curMax > res:
                resIdx = (maxIdx, i)
                res = curMax
            
        return res, nums[resIdx[0]: resIdx[1] + 1]