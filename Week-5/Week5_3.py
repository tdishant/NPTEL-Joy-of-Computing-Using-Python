
import random

door = [0]*3
goatdoor = [0]*2

swap = 0 #number of swap wins
dont_swap = 0 #no of dont swap wins
j = 0
while (j < 20):
    x = random.randint(0, 2) #the door that will have bmw
    
    door[x] = "BMW"
    
    for i in range(0, 3):
        if(i == x):
            continue
        else:
            door[i] = "GOAT"
            goatdoor.append(i)
            
    choice = int(input("Enter your choice : "))
    
    door_open = random.choice(goatdoor) #open a door that doesn't have BMW
    
    while(door_open == choice): #door opened shouldn't be equal to the chosen door 
        door_open = random.choice(goatdoor)    
        
    ch = input("Do you want to swap ? y/n : ")
    
    if ch == 'y':
        if(door[choice] == "GOAT"):
            print("Player Wins")
            swap += 1
        else:
            print("Player Lost")
            
    else:
        if(door[choice] == "BMW"):
            print("Player Wins")
            dont_swap += 1
        else:
            print("Player Lost") 
    j += 1
    
print("Swap wins :", swap)
print("Dont swap wins :", dont_swap)
