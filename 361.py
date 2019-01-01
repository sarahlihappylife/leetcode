class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        lenRow, lenCol = len(grid), len(grid[0])
        res = 0
        rowEnemy = 0
        colEnemy = [0] * lenCol
        for r in xrange(lenRow):
            for c in xrange(lenCol):
                if c == 0 or grid[r][c-1] == 'W':
                    rowEnemy = 0
                    cc = c
                    while cc < lenCol and grid[r][cc] != 'W':
                        rowEnemy += grid[r][cc] == 'E'
                        cc += 1
                    
                if r == 0 or grid[r-1][c] == 'W':
                    colEnemy[c] = 0
                    rr = r
                    while rr < lenRow and grid[rr][c] != 'W':
                        colEnemy[c] += grid[rr][c] == 'E'
                        rr += 1
                
                if grid[r][c] == '0':
                    res = max(res, rowEnemy + colEnemy[c])
        return res