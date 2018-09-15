#!python3
def checkall(i):
    stringed = str(i)
    p = 0
    for c in stringed:
        if(int(c) % 2 == 0 and int(c)!= 0):
            p += 1
        else:
            return -10000
    return 1;


def each_step(i):
    inp = int(input())
    if (checkall(i) != -10000):
        print("Case #" + str(i) +": " + str(0))
        return 0
    step = 1
    p = i+1
    q = i-1
    while(1):
        if((checkall(p) == 1) or (checkall(q) == 1)):
           print("Case #" + str(i) +": " + str(step))
           return 0
        p = p+1
        q = q-1
        step += 1

    


def main():
    cases = int(input())
    i = 1
    while (i<=cases):
        each_step(i)
        i+=1

main()