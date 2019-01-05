class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # # O(n^2) time, O(n) space dp, but now TLE
        # # https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99129/Python-DP-O(n)-space-O(n2)-time
        # n = len(s)
        # dp = [[1] * 2 for _ in range(n)]
        # for j in xrange(1, len(s)):
        #     for i in reversed(xrange(0, j)):
        #         if s[i] == s[j]:
        #             dp[i][j % 2] = 2 + dp[i + 1][(j - 1) % 2] if i + 1 <= j - 1 else 2
        #         else:
        #             dp[i][j % 2] = max(dp[i + 1][j % 2], dp[i][(j - 1) % 2])
        # return dp[0][(n - 1) % 2]
        
        
        # O(n^2), O(n^2) space Memoization
        n = len(s)
        mem = [[None] * n for _ in xrange(n)]
        
        def lenPalindromeSubseq(l, r):
            if l == r:
                return 1
            if l > r:
                return 0
            if mem[l][r]:
                return mem[l][r]
            
            if s[l] == s[r]:
                mem[l][r] = 2 + lenPalindromeSubseq(l+1, r-1)
            else:
                mem[l][r] = max(lenPalindromeSubseq(l+1, r), lenPalindromeSubseq(l, r-1))
            return mem[l][r]
        
        return lenPalindromeSubseq(0, n-1)
        
        
#         # O(2^n) Brute Force, TLE
#         def lenPalindromeSubseq(l, r):
#             if l == r:
#                 return 1
#             if l > r:
#                 return 0
#             return 2 + lenPalindromeSubseq(l+1, r-1) if s[l] == s[r] else max(lenPalindromeSubseq(l+1, r), lenPalindromeSubseq(l, r-1))
        
#         return lenPalindromeSubseq(0, len(s)-1)