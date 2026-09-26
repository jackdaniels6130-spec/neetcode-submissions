class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for item in freq:
            buckets[freq[item]].append(item)
        ans = []
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans