n,m = map(int, input().split())
cards = [int(i) for i in input().split()]
largest = 0

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      temp = cards[i] + cards[j] + cards[k]
      if temp <= m and temp > largest:
        largest = temp

print(largest)
    