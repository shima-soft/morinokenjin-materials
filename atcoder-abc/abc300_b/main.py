H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(input())
B = []
for i in range(H):
    B.append(input())

ans = "No"
for s in range(H):
    for t in range(W):
        same = True
        for i in range(H):
            for j in range(W):
                if A[(i + s) % H][(j + t) % W] != B[i][j]:
                    same = False
        if same:
            ans = "Yes"

print(ans)
