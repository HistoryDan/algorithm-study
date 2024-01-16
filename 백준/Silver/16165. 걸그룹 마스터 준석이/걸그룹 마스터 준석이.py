import sys 

table = dict()
n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    team = sys.stdin.readline().rstrip()
    mem_num = int(sys.stdin.readline().rstrip())
    members = [0 for _ in range(mem_num)]
    
    for i in range(mem_num):
        member = sys.stdin.readline().rstrip()
        members[i] = member
    
    members.sort()
    table[team] = members

for _ in range(m):
    query = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        answer = table[query]
        for a in answer: print(a)
    else:
        for key in table.keys():
            if query in table[key]:
                print(key)
                break

