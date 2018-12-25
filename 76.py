class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        setT = set(t)
        filterS = []
        d = {}  
        for i, ch in enumerate(s):
            if ch in setT:
                filterS.append((i, ch))
                d[ch] = 0

        for ch in t:
            if ch not in d:
                return ""
            d[ch] += 1
        
        cntT = len(t)
        start = end = minStartIdx = 0
        minLen = float('inf')
        while end < len(filterS):
            endIdx, endCh = filterS[end]
            d[endCh] -= 1
            if d[endCh] >= 0:
                cntT -= 1

            if cntT == 0:
                while start <= end and cntT == 0:
                    startIdx, startCh = filterS[start]
                    start += 1
                    d[startCh] += 1
                    if d[startCh] > 0:
                        cntT += 1
                curLen = endIdx - startIdx + 1
                if curLen < minLen:
                    minLen = curLen
                    minStartIdx = startIdx    
            end += 1
        
        if minLen == float('inf'):
            return ""
        return s[minStartIdx: minStartIdx + minLen]