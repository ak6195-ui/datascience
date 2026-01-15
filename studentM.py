students = {}

while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Students")
    print("4. Find Topper")
    print("5. Search Student")
    print("6. Exit")
    choice =int(input("Enter choice: "))

    # 1. Add Student
    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    # 2. Update Marks
    elif choice == 2 :
        name = input("Enter student name to update: ")
        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated!")
        else:
            print("Student not found!")

    # 3. Display All Students
    elif choice == 3:
        if not students:
            print("No students available.")
        else:
            for name, marks in students.items():
                print(name, ":", marks)

    # 4. Find Topper
    elif choice == 4 :
        if not students:
            print("No students available.")
        else:
            topper = max(students, key=students.get)
            print("Topper is:", topper, "with", students[topper], "marks")

    # 5. Search Student
    elif choice == 5 :
        name = input("Enter student name to search: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found!")

    # 6. Exit
    elif choice == 6 :
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
