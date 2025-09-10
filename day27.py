from collections import deque

def shortest_path(V, edges, start, end):
    g = [[] for _ in range(V)]
    for u, v in edges: g[u].append(v); g[v].append(u)
    q, vis = deque([(start, 0)]), {start}
    while q:
        node, d = q.popleft()
        if node == end: return d
        for nb in g[node]:
            if nb not in vis:
                vis.add(nb)
                q.append((nb, d + 1))
    return -1
print(shortest_path(5, [[0,1],[0,2],[1,3],[2,3],[3,4]], 0, 4))  # 3
