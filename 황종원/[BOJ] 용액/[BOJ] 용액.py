N = int(input())
liquid = list(map(int, input().spllit()))

spec = float('INF')
spec_left = 0
spec_right = 0

for i in range(N - 1):
    current = liquid[i]
    
    start = i + 1
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        tmp = current + liquid[mid]
        
        if abs(tmp) < spec:
            spec = abs(tmp)
            spec_left = i
            spec_right = mid
            
            if tmp == 0:
                break
                
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(liquid[spec_left], liquid[spec_right])

