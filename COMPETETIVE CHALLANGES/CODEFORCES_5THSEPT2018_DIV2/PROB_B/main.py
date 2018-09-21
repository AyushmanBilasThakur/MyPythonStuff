def printing(arr):
    for i in arr:
        print(i, end = " ")


inp = list(map(int, input().split()))
n = inp[0]
k = inp[1]
turns = 0
turn_seq = []

arr = []
i = 0
while i < n:
    arr.append(False)
    i+=1

mid = n//2
arr[mid] = True
turns += 1
turn_seq.append(mid)

j = mid

while j <= mid + k:
    if(j >= len(arr)):
        break
    arr[j] = True
    j+=1

j = mid

while j >= mid - k:
    if(j < 0):
        break
    arr[j] = True
    j-=1


if(not(False in arr)):
    print(turns)
    printing(turn_seq)


i = 0

while arr[i] == False:
    i+=1

larr = arr[:i]


i = len(arr) - 1

while arr[i] == False:
    i-=1

rarr = arr[i+1:]

print(larr)
print(rarr)
