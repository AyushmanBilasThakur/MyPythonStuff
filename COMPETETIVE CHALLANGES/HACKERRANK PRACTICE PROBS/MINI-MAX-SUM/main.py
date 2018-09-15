def miniMaxSum(arr):
    arr.sort()
    miniSum = 0
    maxSum = 0
    i = 0
    j = 1
    while i <= 3:
        miniSum += arr[i]
        i+=1
    while j <= 4:
        maxSum += arr[j]
        j+=1
    
    print("{} {}".format(miniSum,maxSum))


arr = [1,4,2,3,5]
miniMaxSum(arr)