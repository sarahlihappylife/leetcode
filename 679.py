class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # nums.sort()
        if len(nums) == 1: 
            return abs(nums[0]-24) <= 0.001
        for i in xrange(len(nums) - 1):
            for j in xrange(i+1, len(nums)):
                a, b = nums[i], nums[j]
                rest = [nums[k] for k in xrange(len(nums)) if k != i and k != j]
                for op in [a+b, a-b, b-a, a*b, a and float(b)/a, b and a/float(b)]:
                    if self.judgePoint24([op] + rest):
                        return True
        return False