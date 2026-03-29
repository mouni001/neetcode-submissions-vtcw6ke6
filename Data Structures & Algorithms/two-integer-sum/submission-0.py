class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number in indices:
                indice1 = indices[number]
                return [indice1, i]
            indices[nums[i]] = i

