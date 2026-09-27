N, D = map(int, input().split())
X = list(map(int, input().split()))

P = []
for i in range(N):
    ok = True
    for j in range(N):
        if j != i and abs(X[i] - X[j]) < D:
            ok = False
    if ok:
        P.append(i + 1)

print(len(P))
print(" ".join(map(str, P)))
