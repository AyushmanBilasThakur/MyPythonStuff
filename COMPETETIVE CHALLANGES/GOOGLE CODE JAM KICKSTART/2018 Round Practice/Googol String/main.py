def compliment(string):
    res = ''
    for c in string:
        if(c=='0'):
            
            res += '1'
        else:
            
            res += '0' 
    return res

def modify(st):
    
    st = st + '0' + compliment(st[::-1])
    return st

cases = int(input())
init = "001"
loop = 0
inp1 = []
inp2 = []
while loop < cases:
    i = int(input())
    inp1.append(i)
    loop += 1
inp2 = inp1
inp2.sort()
max = inp2[-1]

a = len(init)
while (a < max):
    init = modify(init)
    a =len(init)


p = 0
while (p<len(inp1)):
    q = p
    print("Case #"+ str(q+1) + ": " + init[inp1[p] - 1])
    p += 1