s1 = input()
s2 = input()
n = len(s1)
cnt = 0
for i in range(n):
    if s2[i] == '1' and s1[i].isalnum():
        cnt += 1
    elif s2[i] == '0' and not s1[i].isalnum():
        cnt += 1
print('%.2f%%' % (cnt / n * 100))
