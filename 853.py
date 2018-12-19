class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        d = {pos: spd for pos, spd in zip (postion, speed)}
#         for i in xrange(len(position)):
#             d[position[i]] = speed[i]
            
#         res = 0
        cnt = 0
        leadtime = 0
#         for pos, speed in sorted(d.items(), reverse = True):
        for pos, speed in sorted(d.iteritems(), reverse = True):
            curtime = float(target - pos) / speed
            if curtime > leadtime:
                leadtime = curtime
#                 res += 1
                cnt += 1
#         return res
        return cnt
