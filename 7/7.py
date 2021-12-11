def part1(nums):
    m = 230859829856293629
    for i in range(len(nums)):
        s = 0
        for j in range(len(nums)):
            s += abs(nums[i] - nums[j])
        m = min(m, s)
    print(m)

def part2(nums: list):
    m = 230859829856293629
    dict = {x : nums.count(x) for x in set(nums)}
    sum_to_n = lambda n: int(n*(n+1)/2)

    for i in range(max(nums)):
        s = 0
        for key in dict.keys():
            s += sum_to_n(abs(key - i))*dict[key]
        m = min(m, s)
    print(m)

with (open('7\\7.in', 'r') as f):
    nums = [int(x) for x in f.readline().strip().split(',')]
    
    part1(nums)
    part2(nums)



