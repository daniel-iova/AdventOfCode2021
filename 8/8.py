def part1(l):
    c = 0
    lenghts = [2, 3, 4, 7]
    for line in l:
        out = line.split('|')[1].split()
        for x in out:
            if len(x) in lenghts:
                c += 1
    print (c)

def decode_input(inp, lengths):
    char_dict = {1 : '', 7: '', 4: ''}
    for x in inp:
        if len(x) in lengths.keys():
            char_dict[lengths[len(x)]] = set(x)
    known_chars = set().union(char_dict[1], char_dict[4], char_dict[7])
    return char_dict[1], known_chars
        
def decode_output(out, set1, kc, lengths):
    num = ''
    for x in out:
        if len(x) not in lengths.keys():
            len1, len2 = len(set(x) - set(kc)), len(set(kc) - set(x))
            has_full_1 = len(set1 & set(x)) == 2
            if (len1 == 2):
                num += '2' if len2 == 2 else '0' if has_full_1 else '6'
            else:
                num += '9' if len2 == 0 else '3' if has_full_1 else '5'
        else:
            num += str(lengths[len(x)])
    return int(num)

def part2(l):
    lengths = {2 : 1, 3 : 7, 4 : 4, 7 : 8 }
    final_num = 0
    for line in l:
        inp, out = line.split('|')
        inp = inp.split()
        out = out.split()
        set1, kc = decode_input(inp, lengths)
        final_num += decode_output(out, set1, kc, lengths)
    print(final_num)

with open('8\\8.in', 'r') as f:
    l = f.readlines()
    part1(l)
    part2(l)