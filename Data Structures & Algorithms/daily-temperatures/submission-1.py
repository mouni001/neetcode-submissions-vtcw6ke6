class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= []
        res = [0]*len(temperatures)
        stack.append((0, temperatures[0]))
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, value = stack.pop()
                res[index] = i - index
            stack.append((i, temperatures[i]))
        return res
        