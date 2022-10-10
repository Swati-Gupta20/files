file="people-excercise.txt"
c=0
with open(file,'r') as files:
    for i in files:
        c+=1
print(c)
