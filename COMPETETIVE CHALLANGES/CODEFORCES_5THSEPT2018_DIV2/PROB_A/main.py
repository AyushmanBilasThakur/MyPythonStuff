def check_possibility(i2,l,cw,cb):
    cost = 0
    i = 0
    j = l-1
    lim = l//2
    while(i <= lim):
        if(j<i):
            break
        if(i == j):
            if(i2[i] == 2):
                if(cw > cb):
                    cost += cb
                else:
                    cost += cw
        
        elif(i2[i] == 2 and i2[j] == 2):
            if(cw > cb):
                cost += cb * 2
            else:
                cost += cw * 2
        elif(i2[i] != 2 and i2[j] != 2):
            if( i2[i] != i2[j] ):
                return -1
        elif(i2[i] == 2):
            if(i2[j] == 0):
                cost += cw
            else: 
                cost += cb
        elif(i2[j] == 2):
            if(i2[i] == 0):
                cost += cw
            else: 
                cost += cb
       
        i += 1
        j -= 1
            
    return cost


def main():
    input1 = list(map(int, input().split()))
    n = input1[0]   
    cost_white = input1[1]
    cost_black = input1[2]  
    input2 = list(map(int, input().split()))
    cost = check_possibility(input2,n,cost_white,cost_black)
    print(cost)

main()