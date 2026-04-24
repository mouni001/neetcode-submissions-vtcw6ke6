class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        for ops in operations:
            if ops == 'C':
                stack.pop()
            elif ops == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                result = num1 + num2
                stack.append(num2)
                stack.append(num1)
                stack.append(result)
            elif ops == 'D':
                num1 = stack.pop()
                result = 2 * num1
                stack.append(num1)
                stack.append(result)
            else:
                stack.append(int(ops))
        return sum(stack)
        