import sys

students = [i for i in range(1,31)]
commited = [0 for i in range(28)]

for i in range(28):
  commit = int(sys.stdin.readline().rstrip())
  commited[i] = commit

not_commited = [s for s in students if s not in commited]
print(min(not_commited))
print(max(not_commited))