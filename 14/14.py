NUM = 40
def get_tree(node, inp, c, occ, prev):
    current = node
    if (c == NUM):
        occ[node[0]] += 1
    else:
        c += 1
        x = inp[node]
        get_tree(node[0] + x, inp, c, occ, current)
        get_tree(x + node[1], inp, c, occ, current)

template = ''
inp = {}
with open('14\\14.in', 'r') as f:
    l = f.readlines()
    template = l[0].strip()
    for x in l[2:]:
        i1, i2 = x.strip().split(' -> ')
        inp[i1] = i2

x = []
for i in range(len(template)-1):
    x.append(template[i:i+2])

freq = {x : 0 for x in inp.values()}

for i in x:
    get_tree(i, inp, 0, freq, '')
freq[template[-1]] += 1

print(max(freq.values()) - min(freq.values()))
