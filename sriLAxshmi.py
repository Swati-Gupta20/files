# a=int(input("enter the students"))
# if a>=15:
#     print("students studying in 12th")
# if a<=15:
#     print("students studying in 10th")

# else:
#     print("not vallid")


# if 0:
#     print("a")
# else:
#     print("b")


print("WELCOME TO KBC")
name=input("enter your name:")
ques=["1.how many continents are there?"," 2.what is the  capital of india?","3.ng mei koaun se course padhaya jaata hai?"]
option=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.software engineering","2.counseling","3.torium","4.agriculture"]]
solu=[3,4,1]
life_line=[["1.four","2.seven"],["1.bhopal","2.delhi"],["1.softeware engineering","2.counseling"]]
life_solution=[2,2,1]
i=0
def solution(i):
    choose=int(input("enter your choice..."))
    if choose==solu[i]:
        print("congrats")
    else:
        print("try again")
def question():
    i=0
    while i<len(ques):
        print(ques[i])
        j=0
        while j<len(option[i]):
            print(option[i][j])
            j=j+1
        b=solution(i)
        i=i+1
# a=["1.how many continents are there?"," 2.what is the  capital of india?","3.ng mei koaun se course padhaya jaata hai?"]
question()