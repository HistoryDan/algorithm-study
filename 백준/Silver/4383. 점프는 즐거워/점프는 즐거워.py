import sys 

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums == [] : break
    rep = nums[0]
    nums = nums[1:]
    ref = [0 for _ in range(rep)]
    for i in range(rep-1):
        if abs(nums[i]-nums[i+1]) >= 0 and abs(nums[i]-nums[i+1]) <= rep-1:
            ref[abs(nums[i]-nums[i+1])] = 1
    if sum(ref) == rep-1:
        print('Jolly')
    else:
        print('Not jolly')