N = int(input())
S = input()
T = input()

ans = "Yes"
for i in range(N):
    if T[i] != "*" and T[i] != S[i]:
        ans = "No"

print(ans)
