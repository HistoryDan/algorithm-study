import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    tops = [int(i) for i in input().split()]
    bottoms = [int(i) for i in input().split()]
    
    dp_top = [0] * N
    dp_bottom = [0] * N
    dp_none = [0] * N
    dp_top[0], dp_bottom[0] = tops[0], bottoms[0]

    for i in range(1, N):
        dp_top[i] = max(dp_bottom[i-1], dp_none[i-1]) + tops[i]
        dp_bottom[i] = max(dp_top[i-1], dp_none[i-1]) + bottoms[i]
        dp_none[i] = max(dp_bottom[i-1], dp_top[i-1])
    
    print(max(dp_top[N-1], dp_bottom[N-1], dp_none[N-1]))
