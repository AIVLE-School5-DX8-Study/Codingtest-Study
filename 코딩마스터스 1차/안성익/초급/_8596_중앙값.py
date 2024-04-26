import sys
l = list(map(int, sys.stdin.readline().split()))
sys.stdout.write(f'{sorted(l)[2]}')