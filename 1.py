class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not nums or len(nums) < 2:
            return []
        
        d = {}
        
        for i, v in enumerate(nums):
            if v in d:
                return [d[v], i]
            d[target-v] = i
            
        return []