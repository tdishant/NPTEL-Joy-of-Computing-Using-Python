
def rock_paper_scissors(num1, num2, bit1, bit2):
    p1 = int(num1[bit1])%3
    p2 = int(num2[bit2])%3
    
    if(player_one[p1] == player_two[p2]):
        print("Draw")
        
    elif(player_one[p1] == 'Rock' and player_two[p2] == 'Scissors'):
        print("Player 1 wins")
        
    elif(player_one[p1] == 'Rock' and player_two[p2] == 'Paper'):
        print("Player 2 wins")
        
    elif(player_one[p1] == 'Paper' and player_two[p2] == 'Scissors'):
        print("Player 2 wins")
        
    elif(player_one[p1] == 'Paper' and player_two[p2] == 'Rock'):
        print("Player 1 wins")
        
    elif(player_one[p1] == 'Scissors' and player_two[p2] == 'Rock'):
        print("Player 2 wins")
        
    elif(player_one[p1] == 'Scissors' and player_two[p2] == 'Paper'):
        print("Player 1 wins")
        
player_one = {0 : 'Rock', 1 : 'Paper', 2 : 'Scissors'}
player_two = {0 : 'Paper', 1 : 'Rock', 2 : 'Scissors'}

while(1):
    num1 = input("Player one, enter your choice : ")       
    num2 = input("Player two, enter your choice : ")
    
    bit1 = int(input("Plater one, enter the secret bit position : "))
    bit2 = int(input("Plater two, enter the secret bit position : "))
    
    rock_paper_scissors(num1, num2, bit1, bit2)
    
    ch = input("Do you want to continue ? (y/n) : ")
    
    if(ch == 'n'):
        break