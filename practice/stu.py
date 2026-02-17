print("WELCOME : \n")
from use import Studentacc as ss
STUNAME=[]
STUBAL=[]
while  True:
    print("PLEASE ENTER 1 FOR ADDING YOUR NAME :\n")
    print("PLEASE ENTER 2  FOR GOING TO ACCOUNT SERVICE:\n ")
    print("PLEASE ENTER 3 FOR EXIT :")
    CHUS=int(input())
    if CHUS==1:
        print("ENTER YOUR NAME :\n")
        name=input()
        STUNAME.append(name)
        print("SUCESSFUL:\n")
    elif CHUS==2:
        pass 
    elif CHUS==3:
        break
    while True:
        print("ENTER 1 FOR  DEPOSIT \n")
        print("ENTER 2 FOR WITHDRAWL \n")
        print("ENTER 3 FOR EXIT \n")
        print("="*20)
        print("ENTER YOUR OPTION:\n")
        choose=int(input())
        if choose==1:
            print("PLEASE ENTER THE AMOUNT :\n")
            amount=(input())
            ss.deposit(amount)
        elif choose==2:
            print("PLEASE ENTER THE AMOUNT :\n")
            amount=int(input())
            ss.witdraw(amount)
        elif choose==3:
            break
        else:
            print("PLEASE READ AGAIN")