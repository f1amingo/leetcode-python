from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # heap：要排序的堆
        # root：要调整的节点
        # N: 当前数组大小
        def sink(heap, k, N):
            # 左孩子不越界
            while 2 * k + 1 < N:
                j = 2 * k + 1  # 左孩子
                # 找到左右孩子中的最大节点
                if j + 1 < N and heap[j + 1] > heap[j]:
                    j += 1
                # 根节点不小于左右子树，满足堆的要求
                if heap[k] >= heap[j]:
                    break
                heap[k], heap[j] = heap[j], heap[k]
                k = j

        # 建堆，从第一个非叶子结点开始
        for i in range((len(nums) - 1) >> 1, -1, -1):
            sink(nums, i, len(nums))

        # 堆排序，把堆顶和最后一个元素交换
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            sink(nums, 0, i)
        return nums


assert Solution().sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
