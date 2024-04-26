import sys
d = {0:['123X'], 1:['12X3', '1X32'], 2:['X213', 'X132'], 3:['2X13', '31X2'], 4:['231X', '312X'], 5:['23X1', '3X21'], 6:['X321']}

MAT = [sys.stdin.readline().rstrip() for _ in range(2)]
L = MAT[0]+MAT[1]

for key, val in d.items():
    if L in val:
        sys.stdout.write(f'{key}')
        exit()
sys.stdout.write('-1')