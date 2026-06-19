student1 ={"name":"John","Marks":[65,55,85]}
student2 ={"name":"Brad","Marks":[70,80,65]}
student3 ={"name":"David","Marks":[85,75,95]}


StudentDetails =str(input("Enter the Student Name: "))
if StudentDetails == student1["name"]:
    print(f"Marks of  {StudentDetails} are {student1["Marks"]}")
elif StudentDetails == student2["name"]:
        print(f"Marks of  {StudentDetails} are {student2["Marks"]}")
elif StudentDetails == student3["name"]:
            print(f"Marks of  {StudentDetails} are {student3["Marks"]}")

else:
    print("Student not found")