# # # # Level 1 — Basic Printing & Input

# # # # Print your name

# # # # Take user input and print it

# # # # Add two numbers given by user

# # # # Swap two numbers
# # # input1=int((input("enter the number \n")))
# # # input2=input("enter the text \n")
# # # input3=float(input("enter the float value \n"))
# # # print(f"the output are:{input1} \t{input2}\t{input3}")
# # # print("mero nam abi khadka ho ")
# # # name="abi khadka"
# # # print(f"{name.upper()}")
# # # print(f"the sum of two number is:{input1+input3}")
# # # swaap=input1
# # # input1=input3
# # # input3=swaap
  
  
  
# # #   Level 2 — Numerical & Strings

# # # Check even or odd

# # # Convert string to uppercase/lowercase

# # # Count length of string without using len()

# # # Reverse a string (basic slicing)

# # a=int(input("enter the number"))
# # if a%2==0:
# #     print(f"the number is even \t {a}")
# # else:
# #     print("odd")
# # str=input("enter the string \n")
# # str.upper()
# # str.lower()
# # count=0
# # for i in str:
# #     count+=1
# # print(f"the length of string is {count}")
# # print(str[::-1])

# # Level 3 — Lists

# # Create a list & print each element

# # Find largest and smallest element in list

# # Count frequency of an element in list

# # Remove duplicates from list
# # li=[1,2,3,2,2]
# # for i in li:
# #     print(i)
# # print(f"the largest element is {max(li)}")
# # print(f"the samallest element is {min(li)}")
# # print(li.count(2))
# # # li=set(li)
# # print(li)
# # Level 4 — Tuples

# # Check if element exists in tuple

# # Convert list to tuple and vice-versa

# # Find index of element in tuple
# # tup=(1,2,3,)
# # if 2 in tup:
# #     print("yes")

# # li=list(tup)
# # print(li)
# # tup=tuple(li)
# # print(tup)
# # print(tup.index(2))
# # Take student name and marks as input, store in dict

# # Find highest marks from dictionary

# # Update values in dict (e.g. update price, marks etc.)
# # n=(input("enter your name"))
# # m=int(input("enter your marks"))
# # student={n:m}
# # print(student)
# # hig={"abi":90,"ram":80}
# # print(f"the height marks is {max(hig.values())}")
# # hig["abi"]=60
# # print(hig)

# # Display union, intersection, difference of two sets

# # Check if one set is subset of another
# # se={1,2,3,4}
# # es={1,2,3}
# # print(f"the intersection is : {se|es}")
# # print(se.intersection(es))
# # print(se-es)
# # print(se.issuperset(es))


# # Convert integer to binary using bin()

# # Use boolean expressions in conditions (age > 18, etc.)
# a=0
# print(bin(a))
buda_budi={}
while True:
    print("naya nam thapnuxa bhani 1 dabaunus \n")
    print("height update garnu xa bhani 2 dabaunus \n")
    print("nam dekhauna manxa bhani chai 3 dabaunus \n")
    print("exit garna lai 4 dabaunus")
    choice=int(input("\nenter the choice\n"))
    if choice==1:
        name=input("enter the new name\n")
        print("naya height pani halnus ")
        bb_height=int(input("enter the new height\n"))
        buda_budi[name]=bb_height 
        print("completed !!!\n")
    elif choice==2:
        print("enter your name\n")
        name=input()
        if name in buda_budi:
            height=int(input("enter your new height\n"))
            buda_budi[name]=height
            print("updated sucessfully\n")
    
    
    elif choice==3:
        print(buda_budi)
    elif choice==4:
        print("Dhanyebad ")
        break
    else:
        print("error..")

