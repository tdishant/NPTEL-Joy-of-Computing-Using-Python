import calendar

'''
day = calendar.weekday(2001, 2, 27)
print(day)
'''

def get_day(idx):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[idx]

def check_leap(year):
    if(year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
        return True
    else:
        return False

def check_valid_date(date, month, year, leap):
    if leap:
        if(month == 2):
            if(date >= 1 and date <= 29):
                return True
            else:
                return False
        else:
            if(month < 8):
                if(month%2 == 1):
                    if(date >= 1 and date <= 31):
                        return True
                    else:
                        return False
                else:
                    if(date >= 1 and date <= 30):
                        return True
                    else:
                        return False
            else:
                if(month%2 == 0):
                    if(date >= 1 and date <= 31):
                        return True
                    else:
                        return False
                else:
                    if(date >= 1 and date <= 30):
                        return True
                    else:
                        return False
    else:
        if(month == 2):
            if(date >= 1 and date <= 28):
                return True
            else:
                return False
        else:
            if(month < 8):
                if(month%2 == 1):
                    if(date >= 1 and date <= 31):
                        return True
                    else:
                        return False
                else:
                    if(date >= 1 and date <= 30):
                        return True
                    else:
                        return False
            else:
                if(month%2 == 0):
                    if(date >= 1 and date <= 31):
                        return True
                    else:
                        return False
                else:
                    if(date >= 1 and date <= 30):
                        return True
                    else:
                        return False
                    
while(True):
    year = int(input("Enter the year (1970-2021): "))
    if(year >= 1970):
        break
    else:
        print("Enter a valid year from 1970...")

while(True):
    month = int(input("Enter the month (1-12): "))
    if(month >= 1 and month <= 12):
        break
    else:
        print("Enter a valid month in range 1-12...")

leap = check_leap(year)

while(True):
    date = int(input("Enter the date : "))
    if check_valid_date(date, month, year, leap):
        break
    else:
        print("Enter a valid date...")
            
day_index = calendar.weekday(year, month, date)

day = get_day(day_index)
print(date, "/", month, "/", year, "falls on", day)