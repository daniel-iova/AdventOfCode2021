import re

N = 1000

matrix = [ [0 for x in range(N)] for y in range(N)]

s = 0

def when_else(matrix, x1, y1, x2, y2):
    start, end = -1, -1
    start2, end2, step = -1, -1, 1
    if (x1 < x2):
        start, end = x1, x2 + 1
        start2, end2 = y1, y2 + 1
        if (y1 > y2):
            end2 = y2
            step = -1
    else:
        start, end = x2, x1 + 1
        start2, end2 = y2, y1 + 1
        if (y2 > y1):
            end2 = y1
            step = -1
    i = start
    j = start2
    j_cond = (j >= end2) if step == -1 else (j < end2)
    while (i < end and j_cond):
        matrix[j][i] += 1
        i += 1
        j += step
        j_cond = (j >= end2) if step == -1 else (j < end2)
    return matrix

with (open("5\\5.in", "r") as f):

    lines = f.readlines()
    
    for line in lines:
        nums = [int(x) for x in re.sub(" -> ", ',', line).split(',')]
        x1, y1, x2, y2 = nums

        # part 1
        if (x1 == x2):
            for i in range(min(y1, y2), max(y1, y2)+1):
                matrix[i][x1] += 1
        elif (y1 == y2):
            for i in range(min(x1, x2), max(x1, x2)+1):
                matrix[y1][i] += 1
        # part 2
        else:         
            matrix = when_else(matrix, x1, y1, x2, y2)
            
for i in range(N):
    for j in range(N):
        if matrix[i][j] >= 2:
            s += 1

print(s)
