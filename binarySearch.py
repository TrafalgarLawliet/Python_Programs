def binary_search(arr, low, high, x):
     
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid+1
 
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
 

arr = [ 512, 33, 442, 50, 78, 134, 90168, 8087 ]
for x in arr:
    print(x)

print('\n')

arr.sort()

print('Sorted Array:\n')
for x in arr:
    print(x)

myNumber= int(input("Enter the Number to Search: "))
res = binary_search(arr, 0, len(arr)-1, myNumber)
 
if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in array")