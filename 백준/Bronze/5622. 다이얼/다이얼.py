strings = list(input())
number = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
delay = 0
for s in strings:
  delay += number[ord(s)-65]

print(delay)