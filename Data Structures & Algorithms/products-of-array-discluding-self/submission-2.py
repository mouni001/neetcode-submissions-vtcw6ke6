class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] *len(nums)

        total = 1
        for num in nums:
            if num != 0:
                total *= num

        res = [0] * len(nums)
        for num in range(len(nums)):
            if nums.count(0):
                if nums[num] == 0:
                    res[num] = total
            else:
                res[num] = total// nums[num]
        return res


