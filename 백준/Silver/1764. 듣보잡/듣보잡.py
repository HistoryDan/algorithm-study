import sys
input = sys.stdin.readline
n,m = map(int, input().split())

hear = set()
answer = []
for _ in range(n):
    hear.add(input().strip())
for _ in range(m):
    word = input().strip()
    if word in hear:
        answer.append(word)
answer.sort()

print(len(answer))
for i in answer:
    print(i)