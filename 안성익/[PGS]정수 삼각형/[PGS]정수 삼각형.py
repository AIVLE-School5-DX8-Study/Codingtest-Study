def solution(triangle):
    N = len(triangle)
    line_old = triangle[0]
    for line in triangle[1:]:
        for j in range(len(line)):
            if j==0:
                line[j] += line_old[0]
            elif j==(len(line)-1):
                line[j] += line_old[-1]
            else:
                line[j] += max(line_old[j-1], line_old[j])
        line_old = line
    return max(triangle[-1])