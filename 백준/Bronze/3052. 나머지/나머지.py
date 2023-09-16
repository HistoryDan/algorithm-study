import sys
mods = []

for i in range(10):
  num = int(sys.stdin.readline().rstrip())
  mod = num % 42
  if mod not in mods:
    mods.append(mod)

print(len(mods))