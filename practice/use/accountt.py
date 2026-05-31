class  Studentacc:
    def __init__(self,name:list,balance:list):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(self.__balance)
            print("COMPLETE:\n")
        else:
            print("ERROR:\n")
    def witdraw(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            print("sucessful")
            print(self.__balance)
        else:
            print("INSSUFIENT BALANCE :\n")
            
print("sucessful")          