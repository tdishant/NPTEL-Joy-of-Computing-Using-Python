#tuples
ice_cream_flavours = ("vanilla", "chocolate", "butterscotch", "strawberry")
print(ice_cream_flavours)

for i in ice_cream_flavours:
    print(i)

print(ice_cream_flavours[1])

#this gives error as you cannot modify a tuple 
#ice_cream_flavours[2] = "black current"

print(ice_cream_flavours)

#to delete te entire tuple
del ice_cream_flavours

#you add, cannot modify elements, you cannot delete individual elements from tuple
#you can only delete the complete tuple
#thus tuples are immutable

'''you can create a tuple, access elements of a tuple and delete the whole 
tuple'''


toy = (1, 2, 3, 4, 1, 2, 3, 4, 5)

print(len(toy))

toy.count(2)

toy.index(2)

#tuples are used where the item collection remains constant throughout
#example :- image processing
rainbow = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
#pixel = (red, green, blue)
pixel1 = (0.7, 0.1, 0.2)























