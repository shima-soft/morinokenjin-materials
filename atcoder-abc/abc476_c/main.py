import heapq

N = int(input())
A = list(map(int, input().split()))

top = []
out = []
for k in range(N):
    heapq.heappush(top, A[k])
    if len(top) > 3:
        heapq.heappop(top)
    if k >= 2:
        out.append(top[0])

print("\n".join(map(str, out)))
