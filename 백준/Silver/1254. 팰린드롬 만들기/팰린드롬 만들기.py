import sys

def check(string, start, end):
    temp = string[start:end]
    if temp == temp[::-1]:
        return True
    return False

def main():
    string = sys.stdin.readline().rstrip()
    rear = len(string)
    if check(string, 0, len(string)):
        return len(string)
    for i in range(len(string)):
        temp = string + string[:i][::-1]
        if check(temp, i, len(temp)-i):
            return len(temp)

print(main())