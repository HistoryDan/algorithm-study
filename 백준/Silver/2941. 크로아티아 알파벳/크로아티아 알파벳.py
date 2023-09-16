string = input()
check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
total = 0

for c in check:
  total += string.count(c)
  string = string.replace(c,' ')
total += len(string.replace(' ',''))

print(total)