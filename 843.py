# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        
        self.diff = [[sum(ch_i == ch_j for ch_i, ch_j in zip(word_i, word_j)) 
                      for word_j in wordlist] for word_i in wordlist]
        possibleIdx = range(len(wordlist))
        matches = 0
        while matches < 6:
            guessIdx = self.selectGuessIdx(possibleIdx)
            matches = master.guess(wordlist[guessIdx])
            possibleIdx = [idx for idx in possibleIdx if self.diff[guessIdx][idx] == matches]
            
            
    def selectGuessIdx(self, possibleIdx):
        minMaxLen, bestGuessIdx = len(possibleIdx), None
        for guessIdx in possibleIdx:
            matchGroups = [[] for _ in xrange(7)]
            for idx in possibleIdx:
                if idx != guessIdx:
                    matchGroups[self.diff[guessIdx][idx]].append(idx)
            maxMatchGroup = max(matchGroups, key = len)
            if len(maxMatchGroup) < minMaxLen:
                minMaxLen, bestGuessIdx = len(maxMatchGroup), guessIdx
        return bestGuessIdx
    
    
    # def selectGuessIdx(self, possibleIdx):
    #     minCntZeroMatch, bestGuessIdx = len(possibleIdx), None
    #     for guessIdx in possibleIdx:
    #         cntZeroMatch = 0
    #         for idx in possibleIdx:
    #             if self.diff[guessIdx][idx] == 0: 
    #                 cntZeroMatch += 1 
    #         if cntZeroMatch < minCntZeroMatch:
    #             minCntZeroMatch, bestGuessIdx = cntZeroMatch, guessIdx
    #     return bestGuessIdx