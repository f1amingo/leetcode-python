class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif i == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif i == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(i)
        return len(stack) == 0


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("]"))
