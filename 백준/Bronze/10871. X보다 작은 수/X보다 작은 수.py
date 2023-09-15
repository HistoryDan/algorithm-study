n, x = map(int, input().split())
numbers = [int(i) for i in input().split()]
smaller = []

for num in numbers:
  if num < x:
    smaller.append(str(num))

print(' '.join(smaller))