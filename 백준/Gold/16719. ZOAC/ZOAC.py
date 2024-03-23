string = input().rstrip()
ref = [0 for _ in range(len(string))]
cnt = 0

def f(start, stop):
    if start >= stop: return
    
    global string, ref, cnt
    smallest = 'a'
    idx = -1 
    for i in range(start, stop):
        if string[i] < smallest:
            smallest = string[i]
            idx = i
    ref[idx] = cnt
    cnt += 1
    f(idx+1, stop)
    f(start, idx)

f(0,len(string))
for i in range(len(string)):
    ans = ''
    for r in ref:
        if r in [k for k in range(i+1)]:
            ans += string[ref.index(r)]
    print(ans)