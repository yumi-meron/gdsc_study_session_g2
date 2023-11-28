students = {}
print("MENU\n 1. Add a Student.\n 2. View Student.\n 3.List All Students.\n 4.Update Student.\n 5.Delete Student. ")
choice = "yes"

while choice == "yes":
    menu_choice = int(input("what function do you want to do from the menu.\n"))
    
    if menu_choice == 1:
        n= int(input("how many students do you want to register.\n"))
        for i in range(n):
            student_details = {}
            student_details['name'] = input(f"Enter name of student {i+1}: ")
            student_details['age'] = input(f"Enter age of student {i+1}: ")
            student_details['grade'] = input(f"Enter grade of student {i+1}: ")

            students[student_details['name']] = student_details
        choice = input("do you want to continue? 'yes' or 'no'.\n")


    elif menu_choice == 2:
        name = input("Enter student name to be viewed: ")
        if name in students:
            print(f"Name: {name}, Age: {students[name][0]}, Grade: {students[name][1]}")
        else:
            print("Student not found.")
        choice = input("do you want to continue? 'yes' or 'no'.\n")


    elif menu_choice == 3:
        print("Here is the list of students.")
        for key in students.keys():
            print(f"Name: {key}, Age: {students[key][0]}, Grade: {students[key][1]}")
        choice = input("do you want to continue? 'yes' or 'no'.\n")


    elif menu_choice == 4:
        name = input("enter student name to be updated.\n")
        if name in students:
            students[name][0] = input("Updated Age: ")
            students[name][1] = input("Updated Grade: ")
        choice = input("do you want to continue? 'yes' or 'no'.\n") 

        
    elif menu_choice == 5:   
        name = input("enter student name to be deleted.\n")
        if name in students:
            del students[name]
        choice = input("do you want to continue? 'yes' or 'no'.\n") 



        


            
