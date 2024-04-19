import sys
s = 'RUN' if sys.stdin.readline().rstrip() in ('1', '3', '5', '7') else 'STAY'
sys.stdout.write(s)