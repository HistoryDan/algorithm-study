import sys

def roundUp(a):
    if a >= 0:
        rem = a % 1
        if rem >= 0.5:
            return int(a+1)
        else:
            return int(a)
    else:
        rem = a % 1
        if rem > 0.5:
            return int(a)
        elif rem == 0:
            return int(a)
        else:
            return int(a-1)

n = int(sys.stdin.readline().rstrip())
nums = [0 for _ in range(n)]
radix = [0 for _ in range(-4000,4001)]

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums[i] = num
    radix[(num+4000)] += 1

nums = sorted(nums)
total = sum(nums)
mostCounted = max(radix)
cb = 0
if radix.count(mostCounted) > 1:
    cb = radix.index(mostCounted,radix.index(mostCounted)+1) - 4000
else:
    cb = radix.index(mostCounted) - 4000

print(roundUp((total/n)))
print(nums[(n-1)//2])
print(cb)
print(nums[-1] - nums[0])


