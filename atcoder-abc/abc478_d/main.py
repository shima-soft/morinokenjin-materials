N, Q = map(int, input().split())
groups = [[] for _ in range(Q + 1)]
for _ in range(Q):
    L, R, X = map(int, input().split())
    groups[X].append((L, R))

diff = [0] * (N + 2)
for X in range(1, Q + 1):
    groups[X].sort()
    done = 0
    for L, R in groups[X]:
        start = max(L, done + 1)
        if start <= R:
            diff[start] += 1
            diff[R + 1] -= 1
            done = R

ans = []
count = 0
for i in range(1, N + 1):
    count += diff[i]
    ans.append(count)
print(*ans)
