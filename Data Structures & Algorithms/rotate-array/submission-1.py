class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copie = nums[:]
        n = len(nums)
        for i, a in enumerate(copie):
            new_index = (i + k) % n
            nums[new_index] = a
        