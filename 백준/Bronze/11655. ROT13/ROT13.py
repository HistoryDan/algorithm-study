import sys

line = sys.stdin.readline().rstrip()
answer = ''

for i in range(len(line)):
    char = line[i]

    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(line[i]) + 13
        if char > 90:
            char = 64 + char - 90
        char = chr(char)
        
    elif ord(char) <= 122 and ord(char) >= 97:
        char = ord(line[i]) + 13
        if char > 122:
            char = 96 + char - 122
        char = chr(char)

    answer += char

print(answer)