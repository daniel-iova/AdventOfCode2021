DAYS = 256

DAYS += 1
day = [[0 for x in range(9)] for y in range(DAYS)]

with open("6\\6.in", "r") as f:

    nums = [int(x) for x in f.readline().split(',')]
    
    n = len(nums)

    for num in nums:
        day[0][num] += 1
    
    for j in range(1, DAYS): 

        for i in range(1, 9):
            day[j][i-1] = day[j-1][i]
        day[j][8] = day[j-1][0]
        day[j][6] += day[j-1][0]

    print (sum(day[-1]))


    


