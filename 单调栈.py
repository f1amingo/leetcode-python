num = int(input())
num_list = list(map(int, input().split()))
# num = 5
# num_list = [3, 4, 2, 7, 5]

res = [-1] * num

stk = []

for i in range(num - 1, -1, -1):
    while stk and num_list[stk[-1]] > num_list[i]:
        res[stk.pop()] = num_list[i]
    stk.append(i)

print(' '.join(map(str, res)))
