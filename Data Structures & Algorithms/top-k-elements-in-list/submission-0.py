class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        ans = []
        map_sorted = sorted(map.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(map_sorted[i][0])
        return ans