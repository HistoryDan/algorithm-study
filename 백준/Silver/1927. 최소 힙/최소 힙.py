import sys
import heapq
input = sys.stdin.readline

min_heap = []
N = int(input())
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, x)