def ad(p, arr, arr2):
    i = 0
    j = 0
    s = 0
    l = len(arr)
    while(i < l):
        if(i+p < l):
            j = i
            while(j<=i + p):
                s += arr[j]
                j += 1
            arr2.append(s)
        s = 0
        i += 1

def arr_prep(at):
    arr = at
    arr2 = []
    x = 0
    lt = len(arr)
    Low = 0 
    High = 0
    while (x<lt):
        ad(x, arr , arr2)
        x += 1
    arr2.sort()
    return arr2
 
def eachcase():   
    ne_arr_init = input().split()
    ne_arr = int(ne_arr_init[0])
    query = int(ne_arr_init[1])
    a = 0
    ast = input().split()
    arr = []
    arr2 = []
    while (a<ne_arr):
        arr.append(int(ast[a]))
        a += 1
    arr2 = arr_prep(arr)
    qd = 0
    while (qd < query):
        finalout(arr2)
        qd += 1

def finalout(arr2):
    ran = input().split()
    Low = int(ran[0])
    High = int(ran[1]) 
        
    b = Low - 1
    sumout = 0
    while (b<High):
        sumout += arr2[b]
        b += 1
    print(sumout)
    
case = int(input())
vd = 1
while vd <= case:
    print("Case #" + str(vd) + ": ")
    eachcase()
    vd += 1