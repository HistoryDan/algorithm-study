string = input()
result = [-1 for i in range(26)]

for i in range(ord('a'), ord('z')+1):
  if chr(i) in string:
    result[i - ord('a')] = string.find(chr(i))

print(*result)