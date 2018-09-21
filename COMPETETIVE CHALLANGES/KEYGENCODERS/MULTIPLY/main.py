arr_len = input()

arr = list(map(int, input().split(' ')))

test_case = int(input())

i = 0 

while i < test_case:
    res = 1
    limit = list(map(int, input().split(' ')))

    j = limit[0]

    while j <= limit[1]:
        res *= arr[j]
        j+=1

    print(str(res))
    i += 1