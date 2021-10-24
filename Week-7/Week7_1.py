from PIL import Image
import random

end = 100

def check_ladder(points):
    if points == 1:
        print("Ladder")
        return 38
    
    elif points == 4:
        print("Ladder")
        return 14
    
    elif points == 8:
        print("Ladder")
        return 10
    
    elif points == 21:
        print("Ladder")
        return 42
    
    elif points == 28:
        print("Ladder")
        return 76
    
    elif points == 50:
        print("Ladder")
        return 67
    
    elif points == 71:
        print("Ladder")
        return 92
    
    elif points == 80:
        print("Ladder")
        return 99
    
    else:
        return points
        
def check_snake(points):
    if points == 97:
        print("Snake")
        return 78
    
    elif points == 95:
        print("Snake")
        return 56
    
    elif points == 88:
        print("Snake")
        return 24
    
    elif points == 62:
        print("Snake")
        return 18
    
    elif points == 48:
        print("Snake")
        return 26
    
    elif points == 36:
        print("Snake")
        return 6
    
    elif points == 32:
        print("Snake")
        return 10
    
    else:
        return points
    
def reached_end(points):
    
    if(points == end):
        return True
    else:
        return False
    
def show_board():
    img = Image.open('slb.jpg')
    img.show()
    
def play():
    p1_name = input("Player 1 Enter your name : ")
    p2_name = input("Player 2 Enter your name : ")
    
    #Points
    pp1 = 0
    pp2 = 0
    
    turn = 0
    
    while(1):
        if(turn % 2 == 0):
            #Player 1 turn
            print(p1_name, "Your turn...")
            c = int(input("Press 1 to continue, 0 to quit"))
            
            if(c == 0):
                print(p1_name, "scored", pp1)
                print(p2_name, "scored", pp2)
                print("Quitting the game thanks for playing...")
                break
            
            dice =  random.randint(1, 6)
            print("Dice showed :", dice)
            pp1 += dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            
            if(pp1 > end):
                pp1 = end
              
            print(p1_name,"your score is :", pp1) 
            
            if(reached_end(pp1)):
                print(p1_name, "won...")
                break
        
        else:
            print(p2_name, "Your turn...")
            c = int(input("Press 1 to continue, 0 to quit"))
            
            if(c == 0):
                print(p1_name, "scored", pp1)
                print(p2_name, "scored", pp2)
                print("Quitting the game thanks for playing...")
                break
            
            dice =  random.randint(1, 6)
            print("Dice showed :", dice)
            pp2 += dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            
            if(pp2 > end):
                pp2 = end
              
            print(p2_name,"your score is :", pp2) 
            
            if(reached_end(pp2)):
                print(p2_name, "won...")
                break
                
        turn += 1
                
show_board()
play()                
                