
N = 5

def check_max(m, global_min, global_max, changed, changed2):
    if (m < global_min):
        global_min = m
        changed = True

    if (m > global_max):
        global_max = m
        changed2 = True
    
    return global_min, global_max, changed, changed2

def solve(lines : list[str]):

    draws = [int(x) for x in lines[0].split(sep = ',')]
    lines = [x.strip() for x in lines[2:] if x.strip() != '']

    global_min = 358295723089572385
    global_max = -358295723089572385
    global_ans = -1
    global_ans2 = -1

    c = 0
    for i in range(0, len(lines), N):
        matrix = [int(x) for line in lines[i: i+N] for x in line.strip().split()]
        
        changed = False
        changed2 = False

        for l in range(len(draws)):
            ok = False
            for j in range(N):
                row = [matrix[j*N + k] for k in range(N)]
                col = [matrix[j + k*N] for k in range(N)]

                if (set(row).issubset(set(draws[:l+1]))):
                    m = max([draws.index(x) for x in row])
                    global_min, global_max, changed, changed2 = check_max(m, global_min, global_max, changed, changed2)
                    ok = True

                if (set(col).issubset(set(draws[:l+1]))):
                    m = max([ draws.index(x) for x in col])
                    global_min, global_max, changed, changed2 = check_max(m, global_min, global_max, changed, changed2)
                    ok = True
                if ok:
                    break
            if ok:
                break
        
        if changed:
            global_ans = (sum(matrix) - sum([x for x in draws[:global_min+1] if x in matrix])) * draws[global_min]

        if changed2:
            global_ans2 = (sum(matrix) - sum([x for x in draws[:global_max+1] if x in matrix])) * draws[global_max]
        c += 1
    
    print(global_ans, global_ans2)


with (open("4\\4.in", "r") as f):
    lines = f.readlines()
    solve(lines)