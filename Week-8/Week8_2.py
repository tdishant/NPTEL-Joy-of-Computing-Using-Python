import random
import matplotlib.pyplot as plt

days = 0
account = 0
x = []
y = []
while(days != 365):
    x.append(days + 1)
    bet = random.randint(1, 10)
    #print("Bet :", bet)
    lucky_draw = random.randint(1, 10)
    #print("Luckey Draw :", lucky_draw)
    
    if(bet == lucky_draw):
        account += 900 - 100
    else:
        account -= 100

    #print("Amount in your account :", account)
    y.append(account)
    
    days += 1

plt.plot(x, y, "b-")
plt.show()

print("Amount in your account :", account)