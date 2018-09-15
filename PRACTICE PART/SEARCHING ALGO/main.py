#THE GIVEN ARRAY NEEDS TO BE SORTED ALREADY TO PERFORM BUBBLE SORT

def binary_search(arr,val):
    l = len(arr)
    if l == 0 or (l == 1 and arr[0] != val):
        return False

    mid = arr[len(arr)/2]
    if val == mid:
        return True
    if val<mid: 
        binary_search(arr[:l/2], val)
    if val>mid: 
        binary_search(arr[l/2+1:], val)

a = [1,2,3,4,5,6,7,8,9]
while(True):
    i = int(input())
    if(i == 9999):
        break
    binary_search(a,i)
