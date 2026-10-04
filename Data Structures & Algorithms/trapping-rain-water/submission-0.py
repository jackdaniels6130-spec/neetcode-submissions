class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftList = [0]
        currLeftMax = height[0]
        for i in range(1, len(height)):
            maxLeftList.append(currLeftMax)
            if height[i] > currLeftMax:
                currLeftMax = height[i]
        
        maxRightList = [0]
        currRightMax = height[-1]
        for i in range(len(height)-2, -1, -1):
            maxRightList.append(currRightMax)
            if height[i] > currRightMax:
                currRightMax = height[i]
        maxRightList.reverse()

        trappedWater = 0 
        for i in range(len(height)):
            trappedWater += max((min(maxLeftList[i], maxRightList[i]) - height[i]), 0)
        return trappedWater