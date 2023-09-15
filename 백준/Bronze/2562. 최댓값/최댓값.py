largest = 0
idx = 0

for i in range(9):
  num = int(input())
  if num > largest:
    largest = num
    idx = i+1

print(largest)
print(idx)