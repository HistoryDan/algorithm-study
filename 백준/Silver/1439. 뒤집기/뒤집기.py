import sys 
import math

string = sys.stdin.readline().rstrip()
current = string[0]
change_cnt = 0

for i in range(1,len(string)):
    if string[i] != current:
        current = string[i]
        change_cnt += 1

print(math.ceil((change_cnt/2)))