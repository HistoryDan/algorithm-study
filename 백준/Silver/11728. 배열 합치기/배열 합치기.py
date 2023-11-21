import sys 
size_a, size_b = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = [0 for _ in range(size_a + size_b)]
ptr_a = ptr_b = 0
i = 0

while ptr_a < size_a or ptr_b < size_b:
    if ptr_b >= size_b:
        smaller = a[ptr_a]
        ptr_a += 1
    elif ptr_a >= size_a:
        smaller = b[ptr_b]
        ptr_b += 1
    elif a[ptr_a] < b[ptr_b]:
        smaller = a[ptr_a]
        ptr_a += 1
    else:
        smaller = b[ptr_b]
        ptr_b += 1
    c[i] = smaller
    i += 1
print(*c)