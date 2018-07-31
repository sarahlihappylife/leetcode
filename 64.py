class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        total = 0
        ls = []
        for num in grid[0]:
            total += num
            ls.append(total)
        
        for r in xrange(1, len(grid)):
            ls[0] += grid[r][0]
            for c in xrange(1, len(grid[0])):
                ls[c] = grid[r][c] + min(ls[c], ls[c-1])
        return ls[-1]