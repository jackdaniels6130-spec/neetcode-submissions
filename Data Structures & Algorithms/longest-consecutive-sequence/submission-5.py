class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                longest = 1
                while current + 1 in nums:
                    longest += 1
                    current += 1
                max_len = max(longest, max_len)
        return max_len
