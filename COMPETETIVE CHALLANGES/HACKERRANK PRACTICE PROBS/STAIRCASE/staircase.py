def staircase(n):
    p = 0
    q = n-p-1
    r = 0
    while p < n:
        r = 0
        q = n - p - 1
        while q > 0:
            print(' ',end = '')
            q -= 1
        while(r <= p):
            print("#",end = '')
            r += 1
        print()
        p += 1

n = int(input())

staircase(n)