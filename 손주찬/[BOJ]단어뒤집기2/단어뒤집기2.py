def reverse_word(word):
    return word[::-1]

def reverse_words_in_string(S):
    result = []
    is_tag = False
    word = ''
    
    for char in S:
        if char == '<':
            is_tag = True
            if word:
                result.append(reverse_word(word))
                word = ''
            result.append(char)
        elif char == '>':
            is_tag = False
            result.append(char)
        elif char == ' ':
            if not is_tag and word:
                result.append(reverse_word(word))
                word = ''
            result.append(char)
        else:
            if not is_tag:
                word += char
            else:
                result.append(char)
    
    if word:
        result.append(reverse_word(word))
    
    return ''.join(result)

S = input()

print(reverse_words_in_string(S))
