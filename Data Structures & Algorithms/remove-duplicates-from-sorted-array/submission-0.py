class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        position = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[position] = nums[i]
                position += 1

        return position

 #[2,10,10,30,30,40,40]
 # [2,10,30,30,30,40,40]