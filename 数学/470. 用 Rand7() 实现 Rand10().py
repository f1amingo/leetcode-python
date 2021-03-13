# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self) -> int:
        tmp = 49
        while tmp > 40:
            tmp = (rand7() - 1) * 7 + rand7()
        return tmp % 10 + 1
