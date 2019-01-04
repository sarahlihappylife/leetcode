class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # Approach using stack
        heights.append(0)
        idxStack = [-1]
        maxArea = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[idxStack[-1]]:
                h = heights[idxStack.pop()]
                w = i - idxStack[-1] - 1
                maxArea = max(maxArea, h * w)
            idxStack.append(i)
        heights.pop()
        return maxArea
        
        
#         # Approach without stack
#         width = len(heights)
#         left, right = [1] * width, [1] * width
        
#         for i in xrange(width):
#             j = i - 1
#             while j >= 0:
#                 if heights[j] >= heights[i]:
#                     left[i] += left[j]
#                     j -= left[j]
#                 else:
#                     break
        
#         for i in xrange(width - 1, -1, -1):
#             j = i + 1
#             while j < width:
#                 if heights[j] >= heights[i]:
#                     right[i] += right[j]
#                     j += right[j]
#                 else:
#                     break
                    
#         maxArea = 0
#         for i in xrange(width):
#             maxArea = max(maxArea, heights[i] * (left[i] + right[i] - 1))
#         return maxArea