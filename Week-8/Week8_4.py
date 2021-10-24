str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

if(sorted(str1) == sorted(str2)):
    print("The given string are anagrams")
else:
    print("The given strings are not anagrams")