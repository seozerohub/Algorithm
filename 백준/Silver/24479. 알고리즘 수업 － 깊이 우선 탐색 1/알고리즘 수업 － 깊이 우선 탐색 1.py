import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

N,M,v = map(int, input().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N + 1)]
cnt = 1

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global cnt
    visited[v]= cnt
    graph[v].sort()
    for i in graph[v]:
        if visited[i]==0:
            cnt = cnt+1
            dfs(i)

dfs(v)
for i in range(1,N+1):
    print(visited[i])