class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 1: 
            return abs(nums[0]-24) <= 0.001
        
        n = len(nums)
        for i in xrange(n - 1):
            for j in xrange(i+1, n):
                a, b = nums[i], nums[j]
                rest = [nums[k] for k in xrange(n) if k != i and k != j]
                for op in [a+b, a-b, b-a, a*b, a and float(b)/a, b and a/float(b)]:
                    rest.append(op)
                    if self.judgePoint24(rest):
                        return True
                    rest.pop()
        return False