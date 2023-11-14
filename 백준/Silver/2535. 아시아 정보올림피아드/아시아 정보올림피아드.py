import sys
n = int(sys.stdin.readline().rstrip())

entries = []
for _ in range(n):
    entry = list(map(int, sys.stdin.readline().split()))
    entries.append(entry)

largest = 0
answer = []

for entry in entries:
    score = entry[2]
    if score > largest:
        largest = score
        best_entry = entry

entries.remove(best_entry)
answer.append(best_entry)

largest = 0
for entry in entries:
    score = entry[2]
    if score > largest:
        largest = score
        best_entry = entry
entries.remove(best_entry)
answer.append(best_entry)

largest = 0
if answer[0][0] == answer[1][0]:
    for entry in entries:
        if entry[0] == answer[0][0]:
            continue
        else:
            score = entry[2]
            if score > largest:
                largest = score
                best_entry = entry
else: 
    for entry in entries:
        score = entry[2]
        if score > largest:
            largest = score
            best_entry = entry
answer.append(best_entry)

for a in answer:
    print(a[0],a[1])
    
