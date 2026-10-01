class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_numbers = {}
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in dict_numbers:
                return [dict_numbers[answer], i]
            dict_numbers[nums[i]] = i
            
