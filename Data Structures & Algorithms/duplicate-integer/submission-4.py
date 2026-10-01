class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array_set = set()
        for num in nums:
            if num in array_set:
                return True
            array_set.add(num)
        return False
