class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            exor = 0
            for num in nums:
                exor ^= num
            return exor
