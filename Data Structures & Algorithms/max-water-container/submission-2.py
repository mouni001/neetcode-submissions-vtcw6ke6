class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_amount = 0

        while left < right:
            minimum = min(heights[left], heights[right])
            position = right - left
            amount = minimum * position
            if max_amount < amount:
                max_amount = amount
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_amount
