class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def isPair(x, y):
            if x == '(' and y == ')':
                return True
            if x == '[' and y == ']':
                return True
            if x == '{' and y == '}':
                return True
            else:
                return False

        for c in s:
            if c == '(':
                stack.append(c)
            elif c == '[':
                stack.append(c)
            elif c == '{':
                stack.append(c)
            else:
                if len(stack) == 0 or not isPair(stack.pop(), c):
                    return False

        return len(stack) == 0
