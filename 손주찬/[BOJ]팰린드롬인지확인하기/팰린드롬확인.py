def palindrom(word):
    r_word = word[::-1]
    if word == r_word:
        print(1)
    else:
        print(0)

word = input()

palindrom(word)