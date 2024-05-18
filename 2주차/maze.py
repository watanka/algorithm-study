'''
백준 2178번 미로 탐색
'''
from collections import deque

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, list(input()))))

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

queue = deque([(0,0)])
while queue:
    cy, cx = queue.popleft()
    for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
        ny, nx = cy + dy, cx + dx
        
        if (0 <= ny < N and 0 <= nx < M):
            if maze[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((ny, nx))

print(visited[N-1][M-1])