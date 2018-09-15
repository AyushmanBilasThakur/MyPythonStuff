def diagonalDifference(arr,n):
    sul = 0 
    sur = 0
    i = 0
    j = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                sul += arr[i][j]
                      
            if (i+j) == (n-1):
                sur += arr[i][j]  
            j += 1
        i += 1
    res = sul - sur
    if(res < 0):
        res *= -1
    return res


n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
    
result = diagonalDifference(arr,n)

print(result)