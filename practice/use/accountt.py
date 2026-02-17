class  Studentacc:
    def __init__(self,name:list,balance:list):
        self.name=name
        self.__balance=balance
    def deposit(self):
        if self.__balance>0:
            self.__balance+=self.__balance
            print(self.__balance)
            print("COMPLETE:\n")
        else:
            print("ERROR:\n")
    def witdraw(self):
        if self.__balance<=self.__balance:
            self.__balance=self.__balance-self.__balance
            print("sucessful")
            print(self.__balance)
        else:
            print("INSSUFIENT BALANCE :\n")
            
print("sucessful")          