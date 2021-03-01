from typing import List


# 进制转换：给定一个十进制数M，以及需要转换的进制数N。将十进制数M转化为N进制数。
# 输入为一行，M(32位整数)、N(2 ≤ N ≤ 16)，以空格隔开。
def decimal_to_n_base(M: int, N: int) -> str:
    digits = '0123456789ABCDEF'
    flag = False  # 是否负数
    if M < 0:
        flag = True
        M = -M
    res = []
    while M:
        M, mod = divmod(M, N)
        res.append(digits[mod])
    if flag:
        res.append('-')
    res.reverse()
    return ''.join(res)


if __name__ == '__main__':
    assert decimal_to_n_base(7, 2) == '111'
    assert decimal_to_n_base(10, 16) == 'A'
    assert decimal_to_n_base(11, 16) == 'B'
    assert decimal_to_n_base(12, 16) == 'C'
    assert decimal_to_n_base(13, 16) == 'D'
    assert decimal_to_n_base(14, 16) == 'E'


# 1. 十进制(32位int整数)转化为二进制
# 正数：除2取余，逆序排列，符号位0
# 负数，为正数的补码(取反+1)，符号位1
def decimal_to_binary(n: int) -> str:
    # 将正数转化为二进制
    def positive_to_binary_list(p_num: int) -> List:
        _list = []
        while p_num:
            p_num, mod = divmod(p_num, 2)
            _list.append(mod)
        _list.reverse()
        _list = [0] * (32 - len(_list)) + _list
        return _list

    if n < 0:
        digit_list = positive_to_binary_list(-n)
        size = len(digit_list)
        # 取反，第一位符号位不动
        for i in range(1, size):
            digit_list[i] = 1 - digit_list[i]
        # 给最低位加1
        carry = 1
        for i in range(size - 1, 0, -1):
            if carry == 0:
                break
            tmp = carry + digit_list[i]
            carry, digit_list[i] = divmod(tmp, 2)
        # 最高位为符号位1
        digit_list[0] = 1
        return ''.join(map(str, digit_list))
    else:
        return ''.join(map(str, positive_to_binary_list(n)))

        # 2. 二进制转化为十进制(整数)


def binary_to_decimal(s):
    pass


if __name__ == '__main__':
    assert decimal_to_binary(-7) == '11111111111111111111111111111001'
    assert decimal_to_binary(7) == '00000000000000000000000000000111'
