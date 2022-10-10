file=open("people-excercise.txt",'r')
f=file.read()
l=f.split()
c=0
i=0
while i<len(l):
    c+=1
    i+=1
print(c)
print(len(l))