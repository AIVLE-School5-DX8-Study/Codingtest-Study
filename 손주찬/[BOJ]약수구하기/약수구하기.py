def divide(p, q):
    div = []
    for nums in range(1, p+1):
        if p % nums == 0:
           div.append(nums)
    if len(div) < q:
        return 0
    else:
        return div[q-1]

p, q = map(int, input().split())
result = divide(p, q)
print(result)