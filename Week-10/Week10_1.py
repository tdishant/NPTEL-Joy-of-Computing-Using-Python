#to replace a letter in string we use s.replace(old_substring, new_substring)
#to get the index of an element in list we use list_name.index(element_name)

import string

def remove_matching_lettters(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if(l1[i] == l2[j]):
                l1.remove(l1[i])
                l2.remove((l2[j]))
                l = l1 + ['*'] + l2
                return [l, True]
    l = l1 + ['*'] + l2
    return [l, False]

p1 = input("Enter person 1 name : ")
p1 = p1.lower()
p1 = p1.replace(" ", "")

p2 = input("Enter person 2 name : ")
p2 = p2.lower()
p1 = p1.replace(" ", "")

l1 = list(p1)
l2 = list(p2)

proceed = True

while(proceed):
    ret_list = remove_matching_lettters(l1, l2)
    con_list = ret_list[0]
    proceed = ret_list[1]
    star_index = con_list.index('*')
    l1 = con_list[ : star_index]
    l2 = con_list[star_index+1 : ]
    
count = len(l1) + len(l2)
result = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']

while(len(result) > 1):
    split_index = (count % len(result)) - 1
    if split_index >= 0:
        right = result[split_index+1:]
        left = result[:split_index]
        result = right + left
    else:
        result = result[:len(result)-1]
        
print("Result : ", result[0])