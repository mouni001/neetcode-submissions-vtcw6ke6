class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_nums1 = m -1
        last_nums2 = n -1
        right = len(nums1)- 1
        # [10,11,20,20,22,40] [11,22]
        while last_nums2 >= 0:
            if last_nums1 >= 0 and nums1[last_nums1] > nums2[last_nums2]:
                nums1[right] = nums1[last_nums1]
                last_nums1 -= 1
            else:
                nums1[right] = nums2[last_nums2]
                last_nums2 -= 1
            right -= 1



