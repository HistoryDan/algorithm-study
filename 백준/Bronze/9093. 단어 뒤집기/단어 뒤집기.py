t = int(input())

for i in range(t):
    words = input().split()
    new_words = []
    for word in words:
        new_word = [0 for _ in range(len(word))]
        for j in range(len(word)):
            new_word[j] = word[-(j+1)]
        new_word = ''.join(new_word)
        new_words.append(new_word)
    print(' '.join(new_words))