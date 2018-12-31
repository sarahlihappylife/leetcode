# https://www.jianshu.com/p/63f6cf19923d
# https://www.cnblogs.com/snowInPluto/p/5996269.html

from random import randint

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        for i, v in enumerate(self.nums):
            if v == target:
                if randint(0, cnt) == 0:
                    idx = i
                cnt += 1
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)