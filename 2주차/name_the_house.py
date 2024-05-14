'''
백준 2667번. 단지번호붙이기
'''

from collections import deque

## 단지번호붙이기

N = int(input())

maps = []
for _ in range(N) :
    maps.append(list(map(int, list((input())))))
moves = [[1,0], [-1,0], [0,-1], [0,1]]


def bfs(y, x) :
    maps[y][x] = 0
    queue = deque([(y, x)])
    cnt = 1
    while queue :
        cy, cx = queue.popleft()
        for dy, dx in moves :
            ny, nx = cy + dy, cx + dx
            
            if 0 <= ny < N and 0 <= nx < N :
                if maps[ny][nx] == 1:
                    maps[ny][nx] = 0
                    queue.append((ny, nx))
                    cnt += 1
    return cnt
    

result = []
for j in range(N) : # height
    for i in range(N) : # width 
        if maps[j][i] == 1 :
            cnt = bfs(j,i)
            result.append(cnt)

result.sort()

print(len(result))
for cnt in result :
    print(cnt)

