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
            # tmp = [float(v - 1) / 2 if v > 1 else 0 for v in curRow]
            tmp = []
            for v in curRow:
                if v > 1:
                    tmp.append(float(v - 1) / 2)
                else:
                    tmp.append(0)
            # curRow = [a + b for a, b in zip(tmp + [0], [0] + tmp)]
            curRow = [tmp[0]]
            for i in xrange(1, len(tmp)):
                curRow.append(tmp[i - 1] + tmp[i])
            curRow.append(tmp[-1])
        return min(curRow[query_glass], 1)
        
    
        # res = [poured] + [0] * 100
        # for row in xrange(1, query_row + 1):
        #     for glass in xrange(row, -1, -1):
        #         res[glass] = max(res[glass] - 1, 0) / 2.0 + max(res[glass - 1] - 1, 0) / 2.0
        # return min(res[query_glass], 1)