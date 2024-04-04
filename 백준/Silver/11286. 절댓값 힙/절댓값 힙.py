import sys 
import heapq
input = sys.stdin.readline

N = int(input())
abs_heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(x), x))