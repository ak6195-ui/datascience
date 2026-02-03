# # for loop 
# la=[]
# for i in range(1,10):
#     la.append(i**2)
# print(la)
# #comprehension 
# la_=[i**2 for i in range(1,10) if i%2==0]
# print(la_)
# a=["a","b","c"]
# b=["f","g","h"]
# n=[(aa,bb) for aa in a for bb in b]
# print(n)

# dic={"abi":1,"khadka":2,"ola":3,"la":4}
# print(dic)
# ola={c:dic[c] for c in dic if dic[c]%2==0 }
# print(ola)

# dicc={"name":"abi","surname":"khadka","ola":"baby","iscrii":"ho ki kya ho"}
# cc={a:dicc[a] for a in dicc if (len(dicc[a])>3)}
# print(cc)
# n=int(input("enter a number"))
# print(sum(range(1,n+1)))
# sum=0
# for i in range(n):
#     sum+=i
#     if (sum%2==0):
#         print("even")
#     else:
#         print("ödd")
#digit analyzer 
# n=int(input("enter the number"))
# s=str(n)
# print(len(s))
# summ=0
# for i in s:
#     (summ)+=int(i)
#     print(summ)

# if s[::-1]==s:
#     print("yes")
# else:
#     print("not")
# n=int(input("enter number of terms :"))
# a=1
# b=0
# c=0
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     if c%2==0:
#        print(c)
    
# liss=[1,1,2,3,4,5,6,7,8]
# s=set(liss)
# print(s)
# liss.sort()
# print(liss)
# print(max(liss))
# print(min(liss))
# print(sum(liss))  
# sentence=input("enter anything : \n")
# freq={}
# for ch in sentence:
#     freq[ch]=freq.get(ch,0)+1
# print(freq)
# print("PLEASEENTER YOUR PASSWORD : \n")
# PASS=input()
# che={}
# for i in PASS:
#     che[i]=che.get(i,0)+1
    
# print(che)

# for i in che:
#     print(f"{i}:repeats {che[i]} times ")
# tup=(1,2,3,4,5)
# tup=list(tup)
# tup=[i for i in tup if i%2==0]
# print(tup)
# tup=tuple(tup)

    
# def lii(li):
#    eve=[]
#    odd=[]
#    for i in li:
#       if i%2==0:
#          eve.append(i)
#       else:
#          odd.append(i)
#    return eve , odd
# num=list(map(int,input("enter the number:")))
# print(num)
# even,oddd=lii(num)
# print(f"even is{even}")
# print(f"odd is {oddd}")

# odd=[i**2 for i in range(1,100,2)]
# print(odd)

# di={i:i**2 for i in range(1,10)}
# print(di)

# st={a for a in "aeiouu"}
# print(st)


# def surr(num):
#    return num**2

# la=list(map(int,input("enter the number")))
# print(la)
# ok=map(surr,la)
# print(list(ok))

# def eve(num):
#    return num%2==0
# okk=filter(eve,la)
# print(list(okk))
# def li(num):
#    even=[i for i in num if i%2==0]
#    odd=[a for a in num if a%2==1]
#    return even ,odd
# numm=list(map(int,input("enter the list numbers")))
# evenn,oddd=li(numm)
# print(f"the even is :{evenn}")
# print(f"the odd is:{oddd}")

# aa=(lambda a,b:max(a,b))
# print(aa(1,2))

# data={1:2,3:4,5:6}
# data=list(data.items())
# print(data)
# aa= sorted(data,key=lambda a:a[1])
# print(aa)
# a={"a":1,"b":2}
# aaa=max(a,key=a.get)
# print(f"the key  is {aaa} and the value is {a[aaa]} ")
# a={0:0,1:1}
# def fab(n):
#    if n in a:
#       return a[n]
#    else:
#       aa= fab(n-1) + fab(n-2)
#       a[n]=aa
#       return a[n]
# print(fab(70))
# print(a)
# class Student:
#    def __init__(self,name,marks):
#       self.name=name
#       self.marks=marks
#    def gr(self):
#       if self.marks>90:
#          return self.name,"A+"
#       elif self.marks>80 and self.marks<90:
#          return self.name,"A"
#       else:
#          return "kam xaina"
# name=input("enter your name:")
# marks=int(input("enter your marks"))
# aa=Student(name,marks)
# print(aa.gr())
# class Person:
#    def __init__(self,name,age):
#       self.name=name
#       self.age=age

# class EMP(Person):
#    def __init__(self,name,age,salary):
#       super().__init__(name,age)
#       self.salary=salary
#    def sal(self):
#       return "YEARLY SALARY IS:",self.salary*12

# a=EMP("abi",18,120000)
# print(a.sal())
# class Bank:
#    def __init__(self,name,balance=12000,ano=123):
#       self.name=name
#       self.__balance=balance
#       self.ano=ano
#    def depo(self):
#       print("do you want to deposit yes/no")
#       choo=input()
#       if choo=="yes":
#           print("enter deposit amount:")
#           self.depo=int(input())
#           self.__balance=self.__balance + self.depo
          

#    def wit(self):
#        print("do you want to witdrawl yes/no")
#        choos=input()
#        if choos=="yes":
#          print("enter witdrawl number")
#          self.wit=int(input())
#          self.__balance=self.__balance - self.wit
         
      
# print("enter your name\n")
# nam=input()
# print("enter your acno")
# acno=int(input())
# if acno == 123 :
#    bank=Bank(nam,acno)
#    print(bank.depo())
#    print(bank.wit())

#armstrong number
# num=int(input("enter the number :"))
# num2=num
# tot=0
# digits=len(str(num))
# while num2>0:
#    digit=num2%10
#    tot+=digit**digits
#    num2 //=10
# if tot==num:
#     print("yes")
# else:
#    print("no")

# number=int(input("enter the number :"))
# num2=number
# total=0
# digits=len(str(number))
# while num2>0:
#    digit= num2%10
#    total+=digit**digits
#    num2//=10
# if total==number:
#    print("yes")
# else:
#    print("no")
# rev=0
# num3=number
# while num3>0:
#    digit=num3%10
#    rev=rev*10 + digit
#    num3//=10
# if rev==number:
#    print("yes")
# else:
#    print("no")
    
# for i in range(2,number):
#    if number%i==0 :
#       print("not")
#       break
#    else:
#       print("prime number")
# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# for i in range(110):
#    if i>=10:
#       print("yes")
#       break
# else:
#    print("no")

# word="abi khadka is dammi dammi is abi khadka abi"
# word=word.split()
# print(word)
# freq={}
# for i in word:
#    freq[i]= freq.get(i,0)+1
# print(freq)
# maxx=max(freq,key=freq.get)
# print(f"{maxx} is most repeated {freq[maxx]} times")
# a=[[1,2],[1,3,4,5]]
# aa=[item for sublist in a for item in sublist ]
# print(aa)
# print(max(aa))
# print(min(aa))
# dic={ak:ak**2 for ak in aa }
# print(dic)
# lis=[1,2,3,4,5,6,7]
# def filt(n):
#     for i in range(len(n)):
#         if n[i]%2==0:
#             print("even")
#         else:
#             print("no")
# print(filt(lis))
# def eve(n):
#     ret=[]
#     for i in n:
#         if i%2==0:
#             ret.append(i)
#     return ret
# a=eve(lis)
# print(a)
#password validator
# pas=input("enter your password : \n")
# special=["@","#","%"]
# if len(pas)>8:
#     for  i in pas:
#         if i.isupper():
#             print("UPPER CASE FOUND")
#         elif i in special:
#             print("special character found ")
# else:
#     print("enter your password again ")

# data=[10,"20",30,"abc",40]
# la=[]
# for i in data:
#     if isinstance(i,int) :
#         la.append(i)
#     elif isinstance(i,str) and i.isdigit():
#         i=int(i)
#         la.append(i)
# print(la)         
# print(sum(la)/len(la))
# data = {
#     "a": 1,
#     "b": 2,
#     "c": 1,
#     "d": 2
# }
# rev={}
# for key,values  in data.items():
#     if values in rev:
#         rev[values].append(key)
#     else:
#         rev[values]=[key]
# print(rev)
#library
# class Book:
#     def __init__(self):
#         self.book=[]
#     def add(self):
#         self.choo=input("book add garna manxa?:\n")
#         if self.choo=="yes":
#             self.bookname=input("enter the name of book \n")
#             self.book.append(self.bookname)
#             print("sucessfully addef \n")
#         else:
#             print("bhag muji ")
#     def show(self):
#         self.bookname=input("enter the name of book \n")
#         if self.bookname in self.book:
#                 print(self.book)
#         else:
#             print("xaina book ")  

# a=Book()
# a.add() 
# a.show()
# class Employee:
#     def __init__(self):
#         self.name=input("enter your name :")
#         self.salary=int(input("enter your salary "))
#     def bonus(self):
#         if self.salary>50000:
#             self.salary=self.salary+((10/self.salary)*100)
#         else:
#             self.salary=self.salary +((5/self.salary)*100)
#         return f"{self.name} and salary is {self.salary }"  
# a=Employee()
# print(a.bonus())

# print("SHOPPE:\n")
# buy={}
# while True :
#     print("ENTER OPTION 1 FOR ADDING :\n")        
#     print("ENTER OPTION 2 FOR REMOVING :\n") 
#     print("ENTER OPTION 3 FOR VIEWING THE OBJECT:\n")
#     print("ENTER OPTION 4 FOR  VIEWING ALL OBJECTS:\n")       
#     print("ENTER OPTION 5 FOR EXIT :\n")
#     choos=int(input("enter the choice"))
#     if choos == 1:
#         options=input("ENTER YOUR PRODUCT:")
#         quantity=int(input("ENTER THE QUANTITY "))
#         buy[options]=quantity
#         print("sucess!!!")
#     elif choos == 2:
#         options=input("ENTER  WHAT TO REMOVE:")
#         if options in buy:
#             buy.pop(options)
#             print("sucess")
#     elif choos==3:
#         options=input("ENTER THE PRODUCT NAME:")
#         if options  in buy:
#             print(buy[options])
#     elif choos==4:
#         print(buy)
#     elif choos == 5:
#         break
#     else:
#         break
# rate=20
# for i in buy :
#     print ("calculating total :\n")
#     buy[i]=buy[i]*rate
# print(f"TOTAL IS : {buy}")    

from abc import ABC,abstractmethod
class  Account(ABC):
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    @abstractmethod
    def  calculate_interest(self):
        pass
class Savingaccount(Account):
    def calculate_interest(self):
        return  int(self.balance)*0.04
class Currentaccount(Account):
    def  calculate_interest(self):
        return  int(self.balance*0.02)
class Bank(Account):
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    def withdraw(self,amount):
        if  0<amount<=self.balance:
            self.balance-=amount
        else:
            print("paisa pugena")
    def __str__(self):
        return  f"Account holder:{self.name}"
    def __len__(self):
        return int(self.balance)
    def __add__(self,other):
        return self.balance+other
def total(accountt,index=0):
    if index==len(accountt):
        return 0
    return accountt[index].balance+total(accountt,index+1)
account=[]
while True:
    print("do you want to enter the account name and balance :")
    print("yes ko lagi 1 dabaunus")
    print("no ko lagi 2 dabaunus")
    choice=int(input())
    if choice==1:
        print("enter 1 again for saving account:\n")
        print("enter 2 again for current account :\n")
        choice1=int(input())
        if choice1==1:
            name=input("enter your name :\n")
            balance=input("enter your balance \n")
            account.append(Savingaccount(name,balance))
        elif choice1==2:
            name=input("enter your name :\n")
            balance=input("enter your balance \n")
            account.append(Currentaccount(name,balance))
    elif choice==2:
        break 
#interest_list=list(map(lambda acc:acc.calculate_interest(),account))
#print(interest_list)
#print(total(account))
print(account)
print(Bank)

                
        
    
            