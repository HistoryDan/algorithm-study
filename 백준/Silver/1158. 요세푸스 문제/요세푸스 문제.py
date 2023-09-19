n, k = map(int, input().split())
que = [i for i in range(1, n + 1)]
result = []

idx = 0
while len(que):
    idx = (idx + k - 1) % len(que)
    result.append(que.pop(idx))

print('<' + ', '.join(map(str, result)) + '>')