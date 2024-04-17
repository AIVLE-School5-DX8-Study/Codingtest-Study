def solution(slice, n):
    if n % slice == 0:
        pizza = n // slice
    else:
        pizza = n // slice + 1
    return pizza