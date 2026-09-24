class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num_pair = target - nums[i]
            if num_pair in seen:
                return [seen[num_pair], i]
            seen[nums[i]] = i
