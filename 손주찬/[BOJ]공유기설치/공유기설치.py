def gong(houses, C):
    houses.sort()
    start, end = 1, houses[-1] - houses[0]
    
    result = 0
    while start <= end:
        mid = (start + end) // 2 
        count = 1
        
        current_house = houses[0]
        for i in range(1, len(houses)):
            if houses[i] >= current_house + mid:
                count += 1
                current_house = houses[i]
        
        if count >= C:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

print(gong(houses, C))
