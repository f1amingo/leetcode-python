row1 = input().split()
n, m, q = int(row1[0]), int(row1[1]), int(row1[2])
count = [0] * (n + 1)
for _ in range(m):
    edge = input().split()
    u, v = int(edge[0]), int(edge[1])
    count[u] += 1
    count[v] += 1

for _ in range(q):
    swap = input().split()
    u, v = int(swap[0]), int(swap[1])
    count[u], count[v] = count[v], count[u]

print(' '.join(map(str, count[1:])))
