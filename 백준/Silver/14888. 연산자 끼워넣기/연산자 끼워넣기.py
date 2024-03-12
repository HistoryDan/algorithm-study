import sys 
from itertools import permutations

n = int(input())
# nums = [int(i) for i in input().split()]
nums = input().split()
plus, minus, mult, div = map(int, input().split())
operators = ['+'] * plus + ['-'] * minus + ['*'] * mult + ['//'] * div
largest = -1000000000
smallest= +1000000000

for ops in set(permutations(operators)):
    cur = nums[0]
    for i, op in enumerate(ops):
        if op == '//' and int(cur) < 0:
            cur = -1*(-1*int(cur)//int(nums[i+1]))
        else:
            cur = eval(str(cur) + op + nums[i+1])
    if cur > largest: largest = cur
    if cur < smallest: smallest = cur

print(largest)
print(smallest)