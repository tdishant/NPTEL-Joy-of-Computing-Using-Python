a = 7
b = 2

print(a/b)
print(a//b)

#List

shopping = ["Bread", "Coffee", "Sugar"]
print(shopping)

shopping.append("flour")
print(shopping)

shopping.insert(1, "Oil")
print(shopping)

print(len(shopping))

ages = [12, 34, 34, 35, 56, 42, 87, 23, 76, 23, 12, 98, 67, 12, 70, 40]
print(ages.count(12))
print(len(ages))

for i in range(len(shopping)):
    print(shopping[i])
    
ages.sort()
print(ages)

ages.reverse()
print(ages)

students = ["Arun", "Rajesh", "Harish", "Akanksha", "Lakshmi", "Varsh"]
students.sort()
print(students)
students.insert(0, "JOC")
print(students)

#slicing list_name[start_index:end_index+1:step]
print(students[2:5])

#Fizz_Buzz 
# to convert int to string str(integer)
def fizz_buzz(r):
    
    for i in range(r):
        if i%3 == 0 and i%5 == 0:
            print(str(i) + " = Fizz_Buzz")
            
        elif i%3 == 0:
            print(str(i) + " = Fizz")
        
        elif i%5 == 0:
            print(str(i) + " = Buzz")
            
        else:
            print(i)

fizz_buzz(20)

#crowd computing

## way 1
from statistics import mean

estimates = [1000, 1010, 1786, 2000, 1500, 1500, 100, 120, 150, 150, 145]
estimates.sort()

print(estimates)

#tv = int(0.1*len(estimates))

#estimates = estimates[tv:]
#print(estimates)

#estimates = estimates[:len(estimates)-tv]
#print(estimates)

#print(mean(estimates))

## way 2

from scipy import stats

m = stats.trim_mean(estimates, 0.1)

print(m)

#plotting graphs

import matplotlib.pyplot as plt

#passing only y - values
plt.plot([1, 2, 3, 4])

#passing both y - values and x - values
# plot(x_values, y_values)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel("Squares")

#plotting dotted graph
# ro = red dots 
# r-- = red dashes 
# bs = blue squares
# g^ = green triangles
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g^')

# plotting the estimates

import matplotlib.pyplot as plt
import statistics
estimates = [1000, 1010, 1786, 2000, 1500, 1500, 100, 120, 150, 150, 145]

y = []

estimates.sort()
tv = 0.1*len(estimates)
tv = int(tv)
estimates = estimates[tv : len(estimates) - tv]
for i in range(len(estimates)):
    y.append(5)
    
plt.plot(estimates, y, 'r--')
plt.plot([735], [5], 'g^')
plt.plot(statistics.mean(estimates), [5], 'ro')
plt.plot(statistics.median(estimates), [5], 'bs')