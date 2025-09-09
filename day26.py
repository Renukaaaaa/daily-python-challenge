def detect_cycle(V, edges):
    g = [[] for _ in range(V)]
    for u, v in edges: g[u].append(v); g[v].append(u)
    vis = [0]*V

    def dfs(u, p):
        vis[u] = 1
        for v in g[u]:
            if not vis[v]:
                if dfs(v, u): return True
            elif v != p: return True
        return False
    return any(not vis[i] and dfs(i, -1) for i in range(V))

print(detect_cycle(5, [[0,1],[1,2],[2,3],[3,4],[4,0]])) 
