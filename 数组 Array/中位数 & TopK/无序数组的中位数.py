# 题目来源：https://www.lintcode.com/problem/median

# 无序数组，不是数学上的中位数，而是排在中间的数
# 奇数，中间的值；偶数，排序后第N//2个元素
# 1. 排序，O(NlogN)
# 2. 大小为N//2+1的堆
# 3. 快速选择
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        def partition(A, i, j):
            pivot = nums[i]
            m = i
            for k in range(i + 1, j):
                if A[k] < pivot:
                    m += 1
                    A[k], A[m] = A[m], A[k]
            A[i], A[m] = A[m], A[i]
            return m

        def quick_find(A, lo, hi, k):
            if lo < hi:
                m = partition(A, lo, hi)
                if m == k:
                    return A[m]
                elif m < k:
                    return quick_find(A, m + 1, hi, k)
                else:
                    return quick_find(A, lo, m, k)

        return quick_find(nums, 0, len(nums), (len(nums) + 1) // 2 - 1)


assert Solution().median([7, 9, 4, 5]) == 5
assert Solution().median([4, 5, 1, 2, 3]) == 3
