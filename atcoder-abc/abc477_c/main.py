Q = int(input())
S = input()
T = input()
N = len(S)
M = len(T)

start = [0] * N
for i in range(N - M + 1):
    if S[i:i + M] == T:
        start[i] = 1

acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + start[i]

out = []
for _ in range(Q):
    L, R = map(int, input().split())
    first = L - 1
    last = R - M
    if last >= first and acc[last + 1] - acc[first] > 0:
        out.append("Yes")
    else:
        out.append("No")
print("\n".join(out))
