class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums or len(nums) < 3:
            return 
        
        nums.sort()
        res, total, diff = 0, 0, float('inf')
        
        for i in xrange(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total
                else:
                    if abs(total - target) < diff:
                        diff = abs(total - target)
                        res = total
                    if total < target:
                        l += 1
                    else:
                        r -= 1
        
        return res