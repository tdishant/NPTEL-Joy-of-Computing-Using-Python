
#theory of evolution

#import random

#Prints a random integer from 1 - 5 including 1 and 5
#print(random.randint(1, 5))

#Prints a random integer from 1 - 5 including 1 but upto 4
#random.randrange(start, upto_but_not_including, step)
#to generate only odd numbers = random.randrange(1, 10, 2)
#to generate only even numbers = random.randrange(2, 11, 2)
#print(random.randrange(1, 5))

#Prints random decimal numbers from 0 - 1
#print(random.random())

#with open("file1.txt", "r+") as myfile:
    
    #print(myfile.read())
    #myfile.write("I am fine")
    
#myfile.close()

import random

def evolve(x):
    
    ind = random.randint(0, len(x)-1)
    
    #if the value of p = 1 then only change the dna from 0 to 1
    p = random.randint(1, 100)
    
    if p == 1:
        
        if(x[ind] == '0'):
            
            x[ind] = '1'
        
        else:
            
            x[ind] = '0'
    
    
    
with open("dna_data.txt") as myfile:
    
    x = myfile.read()
    
    x = list(x)
    
    for i in range(0, len(x)):
        
        evolve(x)
print(x)