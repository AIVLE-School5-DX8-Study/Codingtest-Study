import sys

def main() -> None:
    N, M = map(int, sys.stdin.readline().split())
    pokemon_to_num = {}
    num_to_pokenmon = {}
    for i in range(1, N+1):
        pokemon = sys.stdin.readline().rstrip()
        pokemon_to_num[pokemon] = str(i)
        num_to_pokenmon[str(i)] = pokemon
    
    questions = [sys.stdin.readline().rstrip() for _ in range(M)]
    
    for question in questions:
        if question.isnumeric():
            print(num_to_pokenmon[question])
        else:
            print(pokemon_to_num[question])

if __name__ == '__main__':
    main()