nums = input().split()
result = []

for num in nums:
  num = int(num)
  num = (100 * (num % 10)) + (10 * (num // 10 % 10)) + num // 100
  result.append(num)
  
print(max(result))