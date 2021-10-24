
import random
import datetime

#to print todays date
#datetime.date.today()

#to print only year
#datetime.date.today().strftime("%Y")

#to print only month
#datetime.date.today().strftime("%B")

#to print only day
#datetime.date.today().strftime("%d")

#to print the week number of the year
#datetime.date.today().strftime("%W")

#to print the week day of the week
#datetime.date.today().strftime("%w")

#to print the day of the year
#datetime.date.today().strftime("%j")

#to print the day of the week
#datetime.date.today().strftime("%A")

#to display the current time
#datetime.datetime.now()

birthday = []
i = 0

while(i < 50):
    year = random.randint(1895, 2021)
    
    leap = 0
    
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        leap = 1
    else:
        leap = 0
    
    month = random.randint(1, 12)
    
#leap year and month = february
    
    if(month == 2 and leap == 1):
        day = random.randint(1, 29)    
    elif(month == 2 and leap == 0):
        day = random.randint(1, 28)
    elif(month == 7 or month == 8):
        day = random.randint(1, 31)
    elif(month % 2 != 0 and month < 7):
        day = random.randint(1, 31)
    elif(month % 2 == 0 and month > 7 and month < 12):
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    dd = datetime.date(year, month, day) 
    #gettig the day of birthday out of 365 days 
    date_of_year = dd.timetuple().tm_yday
    
    i += 1
    birthday.append(date_of_year)

birthday.sort()

for bd in birthday:
    print(bd, end = " ")
    