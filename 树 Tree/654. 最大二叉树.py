# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *


class Solution:
    # others solution
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_value = max(nums)
        max_index = nums.index(max_value)
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return root

    # my solution
    # def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return None
    #
    #     # end excluded
    #     def construct(start: int, end: int) -> TreeNode:
    #         if start >= end:
    #             return None
    #         root_index = start
    #         for i in range(start + 1, end):
    #             if nums[i] > nums[root_index]:
    #                 root_index = i
    #         new_node = TreeNode(nums[root_index])
    #         new_node.left = construct(start, root_index)
    #         new_node.right = construct(root_index + 1, end)
    #         return new_node
    #
    #     return construct(0, len(nums))


roo = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
a = 1
