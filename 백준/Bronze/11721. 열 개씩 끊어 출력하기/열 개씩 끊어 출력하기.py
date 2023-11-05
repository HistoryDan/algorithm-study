import sys 

string = sys.stdin.readline().rstrip()
i = 0
while i < len(string):
    print(string[i:i+10])
    i += 10