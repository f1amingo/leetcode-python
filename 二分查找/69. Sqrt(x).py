class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            # 右中位数避免死循环
            mid = (l + r + 1) >> 1
            # 等号在这里可以取到，所以l=mid
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l


print(Solution().mySqrt(8))
