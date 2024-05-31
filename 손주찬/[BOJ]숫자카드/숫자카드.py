def find_cards(N, cards, M, targets):
    card_set = set(cards)
    result = []
    for target in targets:
        if target in card_set:
            result.append(1)
        else:
            result.append(0)
    return result

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

result = find_cards(N, cards, M, targets)
print(' '.join(map(str, result)))