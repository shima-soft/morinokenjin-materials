N, M = map(int, input().split())

for i in range(N):
    if i < M % N:
        print(M // N + 1)
    else:
        print(M // N)
