class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}

        for index in range(len(numbers)):
            calcul = target - numbers[index]
            if calcul in dictionary:
                return [dictionary[calcul], index + 1]
            index1 = index + 1
            dictionary[numbers[index]] = index1
            