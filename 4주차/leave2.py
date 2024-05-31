'''
백준 15486 퇴사2
'''

import sys
input = sys.stdin.readline
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
	 
# N = 7
# schedule = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
T, P = zip(*schedule)

dp = [0 for _ in range(N+1)]

profit = 0
for start in range(N):
    profit = max(profit, dp[start])
    end =  start + T[start]
    if end <= N:
        dp[end] = max(profit + P[start], dp[end])
    
print(max(dp))
