class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def iterator(string):
            cntBackSpace = 0
            for ch in reversed(string):
                if ch == '#':
                    cntBackSpace += 1
                else:
                    if cntBackSpace > 0:
                        cntBackSpace -= 1
                    else:
                        yield ch
                
        iteratorS, iteratorT = iterator(S), iterator(T)
        chS, chT = next(iteratorS, None), next(iteratorT, None)
        while chS or chT:
            if chS != chT:
                return False
            chS, chT = next(iteratorS, None), next(iteratorT, None)
        return True
        
        
#         def makeStack(string):
#             stack = []
#             for ch in string:
#                 if ch == '#':
#                     if stack:
#                         stack.pop()
#                 else:
#                     stack.append(ch)
#             return stack
                    
#         stackS, stackT = map(makeStack, [S, T])
#         return "".join(stackS) == "".join(stackT)
        
#         # if len(sStack) != len(tStack):
#         #     return False
#         # for chS, chT in zip(sStack, tStack):
#         #     if chS != chT:
#         #         return False
#         # return True