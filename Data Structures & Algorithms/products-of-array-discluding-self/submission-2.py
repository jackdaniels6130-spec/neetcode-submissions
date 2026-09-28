class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        if nums.count(0) > 1:
            return [0 for _ in range(len(nums))]
        for i in nums:
            if i == 0:
                continue
            product *= i
        if 0 not in nums:
            for i in nums:
                    ans.append(int(product/i))
        else:
            zero_index = nums.index(0)
            ans = [0 for i in range(len(nums))]
            ans[zero_index] = product
        return ans




