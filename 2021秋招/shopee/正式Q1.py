def convert(num: str):
    ans = []
    n = len(num)
    for i in range(n):
        idx = n - i - 1
        ans.append(num[idx])
        if (idx - 1) % 3 == 0 and i != n - 1:
            ans.append(',')
    return ''.join(ans[::-1])


# print(convert('1234567'))
print(convert(input()))
