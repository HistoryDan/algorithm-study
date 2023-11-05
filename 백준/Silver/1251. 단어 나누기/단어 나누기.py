import sys 

word = sys.stdin.readline().rstrip()
answers = []

for i in range(len(word)-1):
    for j in range(i+1, len(word)-1):

        first = word[:i+1]
        second = word[i+1:j+1]
        last = word[j+1:]

        first = first[::-1]
        second = second[::-1]
        last = last[::-1]

        answers.append(first + second + last)

answers = sorted(answers)
print(answers[0])
