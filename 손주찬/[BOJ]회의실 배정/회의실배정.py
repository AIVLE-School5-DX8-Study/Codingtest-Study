def max_meetings(N, meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    last_end_time = 0
    count = 0
    
    for start, end in meetings:
        if start >= last_end_time:
            last_end_time = end
            count += 1
    
    return count

N = int(input().strip())
meetings = []

for _ in range(N):
    start, end = map(int, input().strip().split())
    meetings.append((start, end))

print(max_meetings(N, meetings))