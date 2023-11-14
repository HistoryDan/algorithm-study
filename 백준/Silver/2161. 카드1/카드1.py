import sys
n = int(sys.stdin.readline().rstrip())
cards = [i for i in range(1, n+1)]
dropped = []

while len(cards):
    top = cards.pop(0)
    dropped.append(top)
    if len(cards):
        bottom = cards.pop(0)
        cards.append(bottom)

print(*dropped)