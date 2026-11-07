class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res =0 
        l,r = 0, len(heights) - 1
        while l < r:
            width = r-l
            shortest_wall = min(heights[r], heights[l])
            area = width * shortest_wall
            res = max(res,area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res

        