def checkNum(num):
    iterations = 1
    
    while(num != 1):
        if(num % 2 == 0):
            num = num//2
        else:
            num = num*3 + 1
        print(num, iterations)
        iterations += 1

num = int(input("Enter a number : "))
checkNum(num)

