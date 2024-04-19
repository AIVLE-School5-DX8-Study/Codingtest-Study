instr = input()
origin_len = len(instr)//2
for i in range(origin_len+1):
    s = instr[i:origin_len+i]
    if (s[:i]*2 + s[i:origin_len]*2) == instr:
        print(f'YES\n{s}')
        exit()
print('NO')