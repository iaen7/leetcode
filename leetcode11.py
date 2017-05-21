class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Length = len(height)
        i = 0
        j = Length -1
        MaxArea = 0
        while i!= j:
            Area = min(height[i],height[j]) *(j-i)
            if Area > MaxArea:
                MaxArea = Area
            if height[i]>height[j]:
                j -= 1
            elif height[i]<height[j]:
                i += 1
            else:
                if abs(height[i]-height[i+1]) < abs(height[j]-height[j-1]):
                    i += 1
                else:
                    j -= 1
        return MaxArea

solution = Solution()
A = [3,2,1,3]
print solution.maxArea(A)
