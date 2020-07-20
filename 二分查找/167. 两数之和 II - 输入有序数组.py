from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        left, right = 0, len(numbers) - 1
        while left < right:
            # 大了移动右边
            if numbers[left] + numbers[right] > target:
                mid = (left + right) // 2
                # 这里需要等于
                while numbers[left] + numbers[mid] <= target:
                    # 右中位数
                    # 这样mid不会赋值后还是mid
                    mid = (mid + right) // 2 + 1
                # mid还可能取到right，这里保证循环推进
                right = mid - 1
            elif numbers[left] + numbers[right] < target:
                mid = (left + right) // 2
                while numbers[mid] + numbers[right] >= target:
                    # 左中位数，left, mid中左中位数是left
                    # 这样mid不会取到自己，导致死循环
                    mid = (left + mid) // 2
                left = mid + 1
            # 这里放到最后判断，避免跳过答案
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
        return []


print(Solution().twoSum([3, 24, 50, 79, 88, 150, 345], 200))
