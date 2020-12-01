from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                # 找一张5块，一张10块
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                # 找3张5块
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True


assert Solution().lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
assert not Solution().lemonadeChange([10, 10])
assert Solution().lemonadeChange([5, 5, 5, 10, 20])
assert Solution().lemonadeChange([5, 5, 10])
assert not Solution().lemonadeChange([5, 5, 10, 10, 20])
