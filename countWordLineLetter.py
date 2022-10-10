# user=input("enter file name:-")
# user="people.txt"
# file=open(user,'r')
# f=file.read()
# l=f.split()
# cw=0
# clet=0
# clin=0
# p=0
# with open(user,'r') as files:
#     for i in files:
#         clin+=1
# while p<len(l):
#     if l[p]!='-':
#         clet+=len(l[p])
#         cw+=1
#     p+=1
# print(clin,'lines')
# print(cw,'words')
# print(clet,'letters')
# print(l)



# user="people.txt"
# file=open(user,'r')
# cw=0
# clet=0
# clin=0
# with open(user,'r') as files:
#     for i in files:
#         x=i.split('-')
#         cw+=len(x)
#         clin+=1
#         for p in x:

#            clet+=len(p)
#     print(clin,'lines')
#     print(cw,'words')
#     print(clet,'letters')


user="people.txt"
file=open(user,'r')
f=file.read()
word=f.split()
file.close
file=open(user,'r')
line=file.readlines()
i=0
cl=0
cw=0
while i<len(word):
    if word[i]!='-':
        cl+=len(word[i])
        cw+=1
    i+=1
print(len(line))
print(cw)
print(cl)





