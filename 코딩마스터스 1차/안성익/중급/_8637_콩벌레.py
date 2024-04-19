disp = {'top':(0, -1), 'bottom':(0, 1), 'left':(-1, 0), 'right':(1, 0)}
next_dir_counter_clock = {'top':'left', 'bottom':'right', 'left':'bottom', 'right':'top'}
next_dir_clock = {'top':'right', 'bottom':'left', 'left':'top', 'right':'bottom'}

MAP = []
for i in range(10):
    line = input()
    if '2' in line:
        x = line.find('2')
        y = i
    MAP.append(line)

counter_clock = True
cur_dir = 'top'
i = 0
while True:
    i += 1
    if i > 100:
        print('no')
        exit()
    
    dx, dy = disp[cur_dir]
    
    nx = x + dx
    ny = y + dy
    
    if nx > 9 or ny > 9 or nx < 0 or ny < 0:
        break
    
    if MAP[ny][nx] == '1':
        if counter_clock:
            cur_dir = next_dir_counter_clock[cur_dir]
        else:
            cur_dir = next_dir_clock[cur_dir]
        counter_clock = not counter_clock
    dx, dy = disp[cur_dir]
    if MAP[ny][nx] != '1':
        x += dx
        y += dy
    
print('yes')