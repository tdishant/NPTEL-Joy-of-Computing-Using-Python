
def bubble_sort(a): 
    n = len(a)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if(a[j] > a[j+1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                
    print(a)
    
    
def binary_search(a, x):
    
    bubble_sort(a)
    
    low = 0
    high = len(a) - 1
    index = 0
    found = False
    count = 0
    
    while(low <= high):
        
        count += 1
        mid = (low + high) // 2
        
        if(a[mid] == x): 
            index = mid
            found = True
            break
        
        elif(a[mid] > x):
            high = mid - 1
            
        else:
            low = mid + 1
            
            
    if(found):
        print("Your number", x, "found at index", index,"Number of iterations =", count)
    
    else:
        print("Your number", x, "Not Found")
    
arr = [5, 1, 4, 2, 8]
binary_search(arr, 10)

