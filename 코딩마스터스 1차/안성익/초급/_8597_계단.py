import sys
from math import ceil
N, K = map(int, sys.stdin.readline().split())
a, b = ceil((K-N)/3), (N-K)%3
print(a+b)