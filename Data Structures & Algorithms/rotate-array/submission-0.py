class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        places = {}
        n = len(nums)
        for i, a in enumerate(nums):
            places[i] = a
        for i, a in places.items():
            new_index = (i + k) % n
            nums[new_index] = a
        