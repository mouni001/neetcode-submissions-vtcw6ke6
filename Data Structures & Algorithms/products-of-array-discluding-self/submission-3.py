class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        num_zero = nums.count(0)
        total = 1
        
        if num_zero > 1:
            return answer
        elif num_zero == 1:
            for num in nums:
                if num != 0:
                    total *= num
            i = nums.index(0)
            answer[i] = total
        else:
            for num in nums:
                total *= num
            for i in range(len(nums)):
                number = total//nums[i]
                answer[i] = number
        return answer
        