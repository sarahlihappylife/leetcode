class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        
        curRow = [poured]
        for row in xrange(1, query_row + 1):
            tmp = [float(n - 1) / 2 if n > 1 else 0 for n in curRow]
            curRow = [a + b for a, b in zip(tmp + [0], [0] + tmp)]
        return min(curRow[query_glass], 1)
        
        # res = [poured] + [0] * 99
        # for row in xrange(1, query_row + 1):
        #     for glass in xrange(row, -1, -1):
        #         res[glass] = max(res[glass] - 1, 0) / 2.0 + max(res[glass - 1] - 1, 0) / 2.0
        # return min(res[query_glass], 1)