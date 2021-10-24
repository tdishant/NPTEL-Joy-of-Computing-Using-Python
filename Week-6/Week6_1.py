
import string

d = {}
data = ""
for i in range(len(string.ascii_letters)):
    d[string.ascii_letters[i]] = string.ascii_letters[i-1]
    
print(d)

with open("trial.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        if c in d:
            data = d[c] 
        else:
            data = c
        print(data, end="")