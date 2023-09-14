kg = int(input())
iter = kg // 3
total = kg
not_found = True

if kg % 3 == 0:
    total = kg//3
    not_found = False

for three in range(iter):
    rest = kg - 3*three
    if rest % 5 == 0:
        not_found = False
        five = rest // 5
        if (three + five) < total:
            total = three + five

if not_found:
    print(-1)
else:
    print(total)
  
    