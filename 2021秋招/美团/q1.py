def solution(s: str):
    n = len(s)
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] * 10 + int(s[i - 1])
    ans = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            cur = pre[j]
            if i != 0:
                cur = pre[j] - pre[i - 1] * 10 * (j - i)
            if cur % 22 == 0:
                ans += 1
    return ans


print(solution('12221'))
print(solution(input()))
