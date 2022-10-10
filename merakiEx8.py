banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("file-question3.txt",'w')
i=0
while i<len(banks_list):
    f=file.write(banks_list[i]+"\n")
    i+=1
file.close()