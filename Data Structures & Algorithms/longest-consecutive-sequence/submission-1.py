class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cleaned_nums = sorted(set(nums))
        diff_nums = []
        for i in range(1, len(cleaned_nums)):
            diff_nums.append(cleaned_nums[i] - cleaned_nums[i-1])
        counter = 0
        max = 0
        for i in range(len(diff_nums)):
            if diff_nums[i] == 1:
                counter += 1
            else:
                counter = 0
            if max < counter:
                max = counter
        return max + 1