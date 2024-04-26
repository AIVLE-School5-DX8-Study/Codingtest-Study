def str_number_stack(s:str) -> list:
    stack_instr = []
    olds = ' '
    for i in s:
        if olds != i:
            stack_instr.append(1)
        else:
            stack_instr[-1]+=1
        olds = i
    return stack_instr

def possible_list(stack_instr:list, stack_outstr:list,update_string:tuple) -> list:
    temp = []
    for idx, val in enumerate(stack_instr):
        if idx in update_string:
            temp.append(min(val*2, stack_outstr[idx]))
        else:
            temp.append(val)
    return temp

instr = input()
outstr = input()
stack_instr, stack_outstr = str_number_stack(instr), str_number_stack(outstr) 
possible_duplicates = [
    (0,),
    (1,),
    (2,),
    (0,1),
    (1,2)
]

ans = 0
while any(i < j for i, j in zip(stack_instr, stack_outstr)):
    if len(stack_outstr) == 3 and stack_instr[1]*2 <= stack_outstr[1]:
        stack_instr = [min(i*2, stack_outstr[j]) if j in (0, 2) else i*2 for j, i in enumerate(stack_instr)]
    else:
        tmp = []
        for i in possible_duplicates:
            tmp.append(possible_list(stack_instr, stack_outstr, i))
        tmp.sort(key=lambda x: sum(x), reverse=True)
        stack_instr = max(tmp, key=lambda x: sum(x >= y for x, y in zip(x, stack_outstr)))
    ans += 1
print(ans)