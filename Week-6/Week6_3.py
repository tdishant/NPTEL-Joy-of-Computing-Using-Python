#fn + F5 to run the program

def fact_iter(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
        
    return ans

def fact(n):
    
    if(n == 1 or n == 0):
        return 1
    return n * fact(n-1)

print(fact(5))
print(fact_iter(5))