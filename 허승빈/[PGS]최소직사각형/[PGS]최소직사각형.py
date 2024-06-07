def solution(sizes):
    row = []
    col = []
    for size in sizes:
        if size[0] >= size[1]:
            row.append(size[0])
            col.append(size[1])
        else:
            row.append(size[1])
            col.append(size[0])
    return max(row)*max(col)
    
