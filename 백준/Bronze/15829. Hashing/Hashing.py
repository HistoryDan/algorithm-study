import sys

l = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()
sum = 0

# summation 
for i in range(l):
    num = ord(string[i]) - 96
    sum += (num * (31 ** i))

print(sum % 1234567891)