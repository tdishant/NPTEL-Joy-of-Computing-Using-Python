import turtle

turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 5
height = 7

dot_distance = 25

seurat.setpos(-250, 250) 

#(no_of_rows, no_of_cols, matrix)
def spiral(m, n):
    #starting index of row
    k = 0
    #starting index of col
    l = 0
    f = 0
    seurat.color("white")
    
    while(k < m and l < n):
        
        if(f == 1):
            seurat.right(90)
        #printing first row from the remaining rows
        for i in range(l, n):
            seurat.forward(dot_distance)
            #print(a[k][i], end=" ")
        
        k += 1
        f = 1
        
        seurat.right(90)
        #printing the last column from the remaining column
        for j in range(k, m):
            seurat.forward(dot_distance)
            #print(a[j][n-1], end=" ")
        
        n -= 1
        seurat.right(90)
        
        if(k < m):
            #printing last row from remaining rows
            #range(start, end, step)
            for i in range(n-1, l-1, -1):
                seurat.forward(dot_distance)
                #print(a[m-1][i], end=" ")
            
            m -= 1
         
        seurat.right(90)    
        if(l < n):
            #printing the first column from the remaining column
            for j in range(m-1, k-1, -1):
                seurat.forward(dot_distance)
                #print(a[j][l], end=" ")
            
            l += 1
            
'''a = []
count = 1

for i in range(4):
    l = []
    for j in range(4):
        l.append(count)
        count += 1
    a.append(l)'''
    
spiral(20, 20)
turtle.done()