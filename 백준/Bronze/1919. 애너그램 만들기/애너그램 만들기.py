import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
ref_a = [0 for _ in range(26)]
ref_b = [0 for _ in range(26)]

for i in range(len(first)):
    ref_a[ord(first[i])-97] += 1

for i in range(len(second)):
    ref_b[ord(second[i])-97] += 1

answer = 0
for i in range(26):
    diff = abs(ref_a[i] - ref_b[i])
    answer += diff

print(answer)