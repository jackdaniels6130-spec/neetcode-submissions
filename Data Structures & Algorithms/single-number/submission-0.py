class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            single_sum = 0
            seen = set()
            for num in nums:
                if num in seen:
                    single_sum -= num
                else:
                    single_sum += num
                    seen.add(num)
            return single_sum