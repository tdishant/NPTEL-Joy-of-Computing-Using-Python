
#introduction to dictionaries => key : value pair

conversion_factor = {} 

#inserting elements in dictionary
conversion_factor['dollar'] = 75
conversion_factor['euro'] = 80

print(conversion_factor)

print(conversion_factor['euro'])

print(conversion_factor.keys()) 
   
print(conversion_factor.values())

print(conversion_factor.items())

conversion_factor.pop('euro') 
 
conversion_factor['dollar'] = 100

conversion_factor['yen'] = 50

del conversion_factor['yen']