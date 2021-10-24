
import string
import random
#has all the upper and lowercase letters
#print(string.ascii_letters)
symbols = []

symbols = list(string.ascii_letters)

#initialize 5 elemets to zero
card1 = [0]*5
card2 = [0]*5

#postion in the first card that will have same symbol as card 2
pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)

#the charecter wich will be same in both the cards
same_symbol = random.choice(symbols)
symbols.remove(same_symbol)

if(pos1 == pos2):
    card2[pos1] = same_symbol
    card1[pos1] = same_symbol

else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])

i = 0

while(i < 5):
    if(i != pos1 and i != pos2):
        alphabet1 = random.choice(symbols)
        card1[i] = alphabet1
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        card2[i] = alphabet2
        symbols.remove(alphabet2)
        
    i += 1 

print(card1)
print(card2)

ch = input("Spot the similar charecter : ")

if(ch == same_symbol):
    print("Right")
else:
    print("Wrong")