class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openClose= {']': '[', '}': '{', ')': '('}


        for c in s:
            if c in openClose:
                if stack and openClose[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False