def compareTriplets(a, b):
    i = 0
    pa = 0
    pb = 0
    while i<3:
        res = a[i] - b[i]
        if(res > 0):
            pa += 1
        elif(res < 0):
            pb += 1
        i += 1
    arr = [pa,pb]
    return arr


a = [17,28,30]
b = [99,16,8]
result = compareTriplets(a, b)
print(result)