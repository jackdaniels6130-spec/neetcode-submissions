class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cleaned_nums = sorted(set(nums))
        
        counter = 1
        max_len = 1
        for i in range(1, len(cleaned_nums)):
            if cleaned_nums[i] - cleaned_nums[i-1] == 1:
                counter += 1
            else:
                counter = 1
            if max_len < counter:
                max_len = counter

        return max_len