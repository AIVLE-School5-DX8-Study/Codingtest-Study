document = input().strip()
word = input().strip()

count = 0
index = 0

while index <= len(document) - len(word):
    if document[index:index+len(word)] == word:
        count += 1
        index += len(word)
    else:
        index += 1

print(count)