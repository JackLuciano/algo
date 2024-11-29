#https://www.spoj.com/problems/PT07X/

import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

def recursion(cur, parent, isParentCovered, dp, adj):
    if dp[cur][isParentCovered] != -1:
        return dp[cur][isParentCovered]
    
    ret = 0
    if isParentCovered:
        for child in adj[cur]:
            if child != parent:
                ret += recursion(child, cur, False, dp, adj)

        r = 1
        for child in adj[cur]:
            if child != parent:
                r += recursion(child, cur, True, dp, adj)
        
        ret = min(ret, r)
    else:
        ret = 1
        for child in adj[cur]:
            if child != parent:
                ret += recursion(child, cur, True, dp, adj)
    
    dp[cur][isParentCovered] = ret
    return ret

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        adj = defaultdict(list)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        
        dp = [[-1, -1] for _ in range(n + 1)]
        
        r1 = 1
        for child in adj[1]:
            r1 += recursion(child, 1, True, dp, adj)
        
        r2 = 0
        for child in adj[1]:
            r2 += recursion(child, 1, False, dp, adj)
        
        print(min(r1, r2))

if __name__ == "__main__":
    main()