'''
백준 2875번 대회 or 인턴
'''

N, M, K = map(int, input().split())

if N+M == K:

	print(0)

x = min(N//2, M//1)

while (N+M - 3*x) < K:
	x -= 1

print(x)