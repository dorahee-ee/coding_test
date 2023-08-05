n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

def dfs(vertex):
    global vertex_cnt

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)
    
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

cnt_list = [0 for _ in range(n+1)]
for i in range(1, n+1):
    visited = [False for _ in range(n + 1)]
    vertex_cnt = 0
    visited[i] = True
    dfs(i)
    cnt_list[i] = vertex_cnt

max_cnt = max(cnt_list)
answer = [i for i, v in enumerate(cnt_list) if max_cnt == v]
print(*answer)