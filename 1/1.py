
c1 = 0
c2 = 0
BIG_NUM = 3508590289024380893478
with (open("1\\1.in", "r") as f) :
    prev = BIG_NUM
    nums = [int(x) for x in f.readlines()]
    for num in nums:
        if (num > prev):
            c1 += 1
        prev = int(num)

    prev = BIG_NUM
    for i in range (0, len(nums)-2):
        s = nums[i] + nums[i+1] + nums[i+2]
        if (s > prev):
            c2 += 1
        prev = s

print(c1)
print(c2)