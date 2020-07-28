class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        length = len(path)
        if length <= 1:
            return path
        path_stack = []
        this_one = ''
        for i in range(1, length):
            if path[i] != '/':
                this_one = this_one + path[i]
            if path[i] == '/' or i == length - 1:
                if this_one == '..':
                    if len(path_stack) != 0:
                        path_stack.pop()
                elif this_one == '.' or this_one == '/' or this_one == '':
                    pass
                else:
                    path_stack.append(this_one)
                this_one = ''

        res = ''
        for i in path_stack:
            res = res + '/' + i
        if res == '':
            res = '/'
        return res


# print(Solution().simplifyPath('/home//foo/'))
# print(Solution().simplifyPath('/a/./b/../../c/'))
# print(Solution().simplifyPath('/a/../../b/../c//.//'))
print(Solution().simplifyPath('/a//b////c/d//././/..'))
