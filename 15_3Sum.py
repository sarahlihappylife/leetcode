class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        
        # 1st approach still have to go through all combinations, so no time savingwith two pointers; but check duplicates without using set, and space complexity is lower since no addtional dictionary used
        res = []
        for i in xrange(len(nums)-2):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i-1]:
                continue
                
            target = -nums[i]    
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1  
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1           
                elif total > target:
                    r -= 1
                else:
                    l += 1
        return res
        
        
        # 2nd approach
        #res = set()
        #for i, v in enumerate(nums[:-2]):
        #    if v > 0:
        #        break
        #    if i >= 1 and v == nums[i-1]:
        #        continue
        #    d = {}
        #    for num in nums[i+1:]:
        #        if num in d:
        #            temp = (v, -v - num, num)
        #            res.add(temp)
        #        else:
        #            d[(-v - num)] = 0
        #return map(list, res)    