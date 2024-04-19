import sys
import decimal
p, q = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
Context = decimal.Context(prec=N+2, rounding=decimal.ROUND_HALF_UP)
decimal.setcontext(Context)
print(round(decimal.Decimal(p)/decimal.Decimal(q), N))