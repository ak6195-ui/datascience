#  Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
contact={}
while True:
    print("\nWELCOME TO CONTACT BOOK\n")
    print("ENTER THE OPTIONS\n")
    print("PRESS 1 FOR ADDING NEW CONTACT\n")
    print("PRESS 2 FOR VIEWING THE CONTACT\n")
    print("PRESS 3 TO   SEARCH  THE CONTACT\n")
    print("PRESS 4 FOR UPDATING THE CONTACT\n")
    print("PRESS 5 FOR DELETING THE CONTACT\n")
    print("PRESS 6 FOR EXIT\n")
    print("ENTER THE OPTION : ")
    choice=int(input())
    if choice==1:
        print("ENTER YOUR NAME")
        name=input()
        print("ENTER YOUR NUMBER")
        cont=int(input())
        contact[name]=cont
        print("DONE !!!")
    elif choice==2:
        print("\n")
        print(contact)
    elif choice==3:
        print("WHAT IS YOUR NAME:\n")
        name=input()
        if name in contact:
            print(f"{name} YOUR NUMBER IS :{contact[name]}\n")
            print("\n")
        else:
            print("NOT FOUND!!!")
    elif choice==4:
        print("ENTER YOUR NAME: \n")
        name=input()
        if name in contact:
            print("ENTER YOUR NEW PHONE NUMBER: \n")
            new=int(input())
            print("\nDONE !!!\n")
        else:
            print("SORRY NAME NOT FOUND\n")
    elif choice==5:
        print("ENTER YOUR NAME:\n")
        name=input()
        if name in contact:
            contact.pop(name)
            print(contact)
            print("DONE SUCESSFULLY!!")
    elif choice==6:
        print("THANKYOU!!!")
        break
    else:
        print("ERROR...")
