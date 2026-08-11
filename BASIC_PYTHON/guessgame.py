print("you have entered into game \n")
import random
sec=random.randint(1,6)
iin=int(input("ENTER YOUR NUMBER\n"))
i=0
while (iin==sec or i<sec):
  if(iin==sec):
      print(f"CONGRALUATION THE NUMBER IS:{sec}")
      break
  elif(iin>=sec):
      print("OPPS!!! it is greater")
      iin=int(input("AGAIN ENTER THE VALUE: \n"))
      i+=1
  elif (iin<=sec):
      print("OPPS!!! the value is smaller")
      iin=int(input("AGAIN ENTER THE VALUE: \n"))
      i+=1
      
      