import math 
def get_basin(mx, i, j, c):
    mx[i][j] = -1
    c += 1
    if (i - 1 >= 0 and mx[i-1][j] not in [-1, 9] ):
        c = get_basin(mx, i-1, j, c)
    if (i + 1 < len(mx) and mx[i+1][j] not in [-1, 9] ):
        c = get_basin(mx, i+1, j, c)
    if (j - 1 >= 0 and mx[i][j-1] not in [-1, 9]):
        c = get_basin(mx, i, j-1, c)
    if (j + 1 < len(mx[0]) and mx[i][j+1] not in [-1, 9] ):
        c = get_basin(mx, i, j+1, c)
    return c
    
with open('9\\9.in', 'r') as f:
    l = f.readlines()
    mx = []
    for line in l:
        mx.append([int(x) for x in line.strip()])
    risk = 0
    basins = []
    for i in range(len(mx)):
        m = 10
        for j in range(len(mx[0])):
            if ( (mx[i][j] == 9) or (i - 1 >= 0 and mx[i][j] >= mx[i-1][j]) or
                (i + 1 < len(mx) and mx[i][j] >= mx[i+1][j]) or
                (j - 1 >= 0 and mx[i][j] >= mx[i][j-1]) or
                (j + 1 < len(mx[0]) and mx[i][j] >= mx[i][j+1]) ):
                continue
            risk += mx[i][j] + 1
            basins.append(get_basin(mx, i, j, 0))
    print(risk)
    print(math.prod(sorted(basins, reverse=True)[:3]))