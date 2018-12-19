class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        d = {}
        for i in xrange(len(position)):
            d[position[i]] = speed[i]
            
        res = 0
        leadtime = 0
        for pos, speed in sorted(d.items(), reverse = True):
            curtime = float(target - pos) / speed
            if curtime > leadtime:
                leadtime = curtime
                res += 1
        return res