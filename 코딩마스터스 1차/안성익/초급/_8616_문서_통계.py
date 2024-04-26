import sys
s1 = sys.stdin.readline().rstrip()
s2 = s1.replace(' ', '')
s3 = s1.split()
sys.stdout.write(f'{len(s1)}\n')
sys.stdout.write(f'{len(s2)}\n')
sys.stdout.write(f'{len(s3)}')