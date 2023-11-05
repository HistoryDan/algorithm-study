import sys

n = int(sys.stdin.readline().rstrip())

people = [0 for _ in range(n)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    people[i] = (x, y)

rates = []
for person in people:
    others = people.copy()
    others.remove(person)
    rate = 1
    for other in others:
        if other[0] > person[0] and other[1] > person[1]:
            rate += 1
    rates.append(rate)

print(*rates)

            
