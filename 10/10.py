part2_results = []

def process(s, d, score):
    stack = []
    for c in s:
        if c in d.values():
            stack.append(c)
        else:
            if stack[-1] != d[c]:
                return score[c]
            stack.pop()
    if len(stack) != 0:
        part2_results.append(stack[::-1])
        return -1
    return 0

with open('10\\10.in', 'r') as f:
    part1 = 0
    l = f.readlines()
    d = {')':'(', ']':'[', '}':'{', '>':'<'}
    score = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    for line in l:
        c = process(line.strip(), d, score)
        if c != -1: part1 += c
    print(part1)

    score = '([{<'
    part2 = []
    for res in part2_results:
        s = 0
        for ch in res:
            s = s*5 + score.index(ch)+1
        part2.append(s)
    print(sorted(part2)[int(len(part2)/2)])