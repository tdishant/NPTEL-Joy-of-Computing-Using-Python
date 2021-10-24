
#magic square:- 3X3 (nXn but n should be odd) matrix where all the rows, colums and diagonals of the matrix add up to same number
#numbers are from 1, 2, ...., 9 and they cannot repeat

#facts about magic square
#magic number = M = n(n^2+1)/2 ex n = 3 => 3X(3^3+1)/2 = 15

#steps
#1 -> pos(n/2, n-1) = (p, q)
#2 -> pos(p-1, q+1) if row = -1 then row = n-1 if col = n then col = 0
#if pos is not empty then col = col-2 and row = row+1
#if row = -1 and col = n then (row, col) = (0, n-2)
 
def magic_square(n):
    
    magicSquare = []
    
    for i in range(n):
        l = []
        for j in range(n): 
            l.append(0)
        magicSquare.append(l)
        
    for i in range(n):
        for j in range(n): 
            print(magicSquare[i][j], end=" ")
        print()
    
    print()
    
    i = n//2
    j = n - 1
    
    num = n*n
    count = 1
    
    while(count <= num):
        
        if(i == -1 and j == n):
            
            i = 0
            j = n - 2
            
        elif(i < 0):
            
            i = n - 1
            
        elif(j == n):
            
            j = 0
        
        if(magicSquare[i][j] != 0):
            
            i = i+1
            j = j - 2
            continue
        
        else:
            
            magicSquare[i][j] = count
            count += 1
            
        i = i - 1
        j = j + 1
        
    for i in range(n):
        for j in range(n): 
            print(magicSquare[i][j], end=" ")
        print()
        
    print("The sum of each row/column/diagonal is : "+str(n*(n**2+1)/2))
        
magic_square(3)