import sys
from collections import deque
input = sys.stdin.readline

def check(char_list):
    deck = deque(char_list)
    idx = 0
    while len(deck) > 1:
        if deck.pop() != deck.popleft():
            return idx, False
        idx += 1
    return -1, True

T = int(input())
cnt = 0
for _ in range(T):
    string = [c for c in input().rstrip()]
    deck = deque(string)
    idx1, flag1 = check(string)
    if not flag1:
        new_string1 = string[idx1:len(string)-idx1-1]
        new_string2 = string[idx1+1:len(string)-idx1]
        _, flag2 = check(new_string1)
        _, flag3 = check(new_string2)
        if flag2 or flag3:
            print(1)
        else:
            print(2)
    else:
        print(0)