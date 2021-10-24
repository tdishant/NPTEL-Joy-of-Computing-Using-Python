#Permutation - Jumbled Words

import random

#list of words from which the computer can choose

def choose():
    
    words = ["rainbow", "computer", "science", "programming", "mathematics", "player", "condition", "reverse", "water", "board"]
    
    #selects a random word from the list words
    pick = random.choice(words)
    
    return pick
    
def jumble(word):
    
    #random.sample(word, no_of_letters) returns the jumbled letters in the form of a list so join() is used to convert the list back to string
    # "".join() means join when you encounter "" between two elements of the list
    jumbled_word = "".join(random.sample(word, len(word)))
    
    return jumbled_word

def thank(p1, p2, s1, s2):
    
    print(p1, "Your score is :", s1)
    print(p2, "Your score is :", s2)
    
    print("Thanks for playing.. Have a nice day !!")
    
def play():
    
    #player names
    p1name = input("Enter your name Player 1 : ")
    p2name = input("Enter your name Player 2 : ")
    
    #player points
    pp1 = 0
    pp2 = 0
    
    #which players turn it is
    turn = 0
    
    #starting and continuing the game indefinitely untill one does'nt want to play anymore 
    while(1):
        
        #get the question from the computer
        
        #which word the computer has picked to give to the player
        picked_word = choose()
        
        #jumble the picked word to create the question
        question = jumble(picked_word)
        
        #printing the question so it is visible to the players
        print(question)
        
        #when the value of turn is even it is Player 1's turn and when turn is odd it is player 2's turn
        
        #player_1 turn
        if turn%2 == 0:
            
            print(p1name, "Your turn.")
            ans = input("What is on my mind ? : ")
            
            if ans == picked_word:
                
                pp1 += 1
                print("Your score is", pp1)
                
            else:
                
                print("Better luck next time. The correct answer is :", picked_word)
            
            c = int(input("Do you want to continue playing ? 0/1 : "))
            
            if c == 0:
                
                thank(p1name, p2name, pp1, pp2)
                break
        
        #player_2 turn
        else:
            
            print(p2name, "Your turn.")
            ans = input("What is on my mind ? : ")
            
            if ans == picked_word:
                
                pp2 += 1
                print("Your score is", pp2)
                
            else:
                
                print("Better luck next time. The correct answer is :", picked_word)
            
            c = int(input("Do you want to continue playing ? 0/1 : "))
            
            if c == 0:
                
                thank(p1name, p2name, pp1, pp2)
                break
        
        turn += 1
play()    