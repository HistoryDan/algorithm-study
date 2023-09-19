string = input()
result = set()
diff = 1

for _ in range(len(string)):
  for j in range(len(string) - diff + 1):
    result.add(string[j:j+diff])
  diff += 1

print(len(result))