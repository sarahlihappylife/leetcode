class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        horizon = map(max, zip(*grid))
        vertical = map(max, grid)
        
        increase = 0
        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                increase += (min(vertical[r], horizon[c]) - grid[r][c])
        return increase