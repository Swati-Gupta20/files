file=open('question3.txt','r')
delhi=open("delhi.txt",'w')
shimla=open("shimla.txt",'w')
jaipur=open('jaipur.txt','w')
others=open("others.txt",'w')
a=file.read()
b=a.split('\n')
i=0
while(i<len(b)):
    if 'delhi' in b[i]:
        delhi.write(b[i]+'\n')
    elif 'shimla' in b[i]:
        shimla.write(b[i]+'\n')
    elif 'jaipur' in b[i]:
        jaipur.write(b[i]+'\n')
    else:
        others.write(b[i]+'\n')
    i+=1
file.close()

