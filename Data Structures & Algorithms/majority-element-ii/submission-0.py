class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        dictionary = {}
        res = []
        appear = len(nums)//3

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        print(dictionary)
        for val, freq in dictionary.items():
            if freq > appear:
                res.append(val)
        return res
        