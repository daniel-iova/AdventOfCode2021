
def fold(cds, val, type):
    for i in range(len(cds)):
        if (cds[i][type] > val):
            cds[i][type] = val - abs(val - cds[i][type])
    return cds

def print_matrix(cds):
    for i in range(max(cds, key=lambda x: x[0])[0]+1):
        for j in range(max(cds, key=lambda x: x[1])[1]+1):
            print('#' if [i, j] in cds else '.', end='')
        print()

def get_input(l):
    cds, instr = [], []
    for line in l:
        if 'fold' in line:
            instr.append(line[11:].split('='))
        else:
            cds.append([int(x) for x in line.split(',')[::-1]])   
    return cds, instr

with open('13\\13.in', 'r') as f:
    l = [x.strip() for x in f.readlines() if x.strip() != '']
    cds, instr = get_input(l)
    for i in instr:
        type = 1 if i[0] == 'x' else 0
        cds = fold(cds, int(i[1]), type)
    print(len(set([tuple(x) for x in cds])))
    print_matrix(cds)