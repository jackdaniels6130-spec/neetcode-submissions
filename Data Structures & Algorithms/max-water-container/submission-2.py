class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            wd = r - l
            ht = min(height[l], height[r])
            water = wd * ht
            ans = max(ans, water)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans