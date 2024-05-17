'''
백준 1697번 : Hide and Seek
'''
from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    exit()

time = [0 for _ in range(K*2)]

def bfs(x):
    time[x] = 1
    if x == K:
        return
    queue = deque([x])   
    
    while queue:
        cx = queue.popleft()
        for new_x in [ cx*2, cx-1, cx+1]:
            if 0 <= new_x < K*2:
                if not time[new_x]:
                    time[new_x] = time[cx] + 1
                    queue.append(new_x)

    
bfs(N)
print(time[K] - 1)