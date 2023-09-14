word = input()
length = len(word)
check = [0 for i in range(length)]
for i in range(length):
    check[i] = word[length-i-1]
check = "".join(check)

if check == word:
    print(1)
else:
    print(0)