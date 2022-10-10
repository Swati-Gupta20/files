file=open("people-excercise.txt",'r')
f=file.read()
c=0
for i in f:
    c+=len(i)
print(c)


file=open("people-excercise.txt",'r')
f=file.read()
l=f.split()
c=0
i=0
while(i<len(l)):
    j=0
    while(j<len(l[i])):
        c+=1
        j+=1
    i+=1
print(c)


