import sys 

n = int(sys.stdin.readline().rstrip())
cities = [int(i) for i in sys.stdin.readline().rstrip().split()]
prices = [int(i) for i in sys.stdin.readline().rstrip().split()][:-1]

answer = 0
dist = cities[0]
cur = prices[0]

# 현재 도시보다 기름값이 싼 도시까지 가는 기름은 현재 도시에서 채우고 가야함
for i in range(1, n-1):
    if prices[i] < cur:
        answer += (dist * cur)
        cur = prices[i]
        dist = 0
    dist += cities[i]

answer += (dist*cur)
print(answer)