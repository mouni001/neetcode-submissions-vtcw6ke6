class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        end_pointer = len(nums) - 1
        i = 0

        while i <= end_pointer:
            if nums[i] == 0:
                sub = nums[left]
                nums[left] = nums[i]
                nums[i] = sub
                i += 1
                left += 1
            elif nums[i] == 2:
                sub = nums[end_pointer]
                nums[end_pointer] = nums[i]
                nums[i] = sub
                end_pointer -= 1
            else:
                i += 1



        

        