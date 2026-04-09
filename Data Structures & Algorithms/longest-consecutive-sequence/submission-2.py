class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num - 1 not in nums:
                adding = 1
                current = num + 1
                while current in nums:
                    adding += 1
                    current += 1
                if adding > res:
                    res = adding
        return res

