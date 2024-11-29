from collections import deque

def graph(n, m, edges):
    adj = [[] for _ in range(n + 1)]
    
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    visited = [-1] * (n + 1)
    visited[1] = 0
    
    q = deque([1])
    
    # Perform BFS
    while q:
        val = q.popleft()
        if val == n:
            break
        
        for neighbor in adj[val]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[val] + 1
                q.append(neighbor)
    
    return visited[n] if visited[n] != -1 else -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        
        result = graph(n, m, edges)
        print(result)
