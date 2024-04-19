import sys
year, army, mob, stat  = sys.stdin.readline().split()
if year == '0':
    sys.stdout.write('0')
    exit()
if stat == 'Private':
    if year in '1234':
        if mob == 'Y' or army == 'ROKAF':
            sys.stdout.write('28')
            exit()
        else:
            sys.stdout.write('32')
            exit()
    elif mob == 'N':
            sys.stdout.write('20')
            exit()
else:
    sys.stdout.write('28')
    exit()