def solution(array):
    
    my_list = [0] * (max(array)+1)

    for i in array:
        my_list[i] += 1

    n = 0
    num_max = max(my_list)
    for i in my_list:
        if num_max == i:
            n += 1

    if n==1:
        return my_list.index(max(my_list))
    else:
        return -1