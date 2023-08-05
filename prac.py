n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

print(graph)