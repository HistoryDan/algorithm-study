import sys 
import heapq
input = sys.stdin.readline

N = int(input())
max_heap = []
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(max_heap, (-x, x))