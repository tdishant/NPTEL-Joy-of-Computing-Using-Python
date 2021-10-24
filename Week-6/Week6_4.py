def binary_search(arr, low, high, target):
    
    if(low > high):
        return -1
    
    mid = (low + high)//2
    
    if(arr[mid] == target):
        print("Found the element")
    elif(arr[mid] > target):
        return binary_search(arr, low, mid-1, target)
    else:
        return binary_search(arr, mid+1, high, target)
    
arr = [3,6,8,10,17,28,32]
h = len(arr)-1
binary_search(arr, 0, h, 38)

def fib(n):
    
    if(n == 0 or n == 1):
        return n
    return fib(n-1) + fib(n-2)

for i in range(5):
    print(fib(i), end=" ")