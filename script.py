def solute(graph):
    def dfs()
    n = len(graph)
    vis = [False] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:




c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1
    print(solute(graph))
