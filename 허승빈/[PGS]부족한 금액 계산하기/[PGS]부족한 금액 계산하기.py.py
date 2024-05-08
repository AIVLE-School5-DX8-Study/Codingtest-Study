def solution(price, money, count):
    price_sum = []
    for i in range(1, count+1):
        price_su = price * i
        price_sum.append(price_su)
    if money < sum(price_sum):
        return sum(price_sum) - money
    else:
        return 0
        
