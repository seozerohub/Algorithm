from collections import deque
import sys
input = sys.stdin.readline

# 정점의 수 N 간선의 수 M 시작 정점 start
# 정점 u와 정점 v의 가중치 1인 양방향 간선
# i번째 줄에는 정점 i의 방문 순서 출력

N,M,start = map(int, input().split())
graph = [[]for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, N + 1):
    graph[i].sort()

def bfs(graph, start, visited):
    # 시작 노드
    global cnt
    queue = deque([start])
    visited[start]= cnt

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt = cnt +1
                visited[i] = cnt
                queue.append(i)

bfs(graph,start,visited)

for i in range(1,N+1):
    print(visited[i])