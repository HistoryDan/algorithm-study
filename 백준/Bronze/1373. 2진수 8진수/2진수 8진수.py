import sys

binary = sys.stdin.readline().rstrip()
decimal = int(binary, 2)
octal = oct(decimal)[2:]

print(octal)
