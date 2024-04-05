mass = {'H': 1, 'C': 12, 'O': 16}
formula = input().strip()
stack = []

for ch in formula:
    if ch.isalpha():
        stack.append(mass[ch])
    elif ch.isdigit():
        stack[-1] *= int(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        temp = 0
        while stack[-1] != '(':
            temp += stack.pop()
        stack.pop()  # remove '('
        stack.append(temp)

print(sum(stack))