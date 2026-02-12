students = {
    "24811051":{
        "name":"sai",
        "department":"cse",
    },
    "24811052":{
        "name":"henry",
        "department":"cse",
    },
    "24811053":{
        "name":"mani",
        "department":"cse",
    },
    "24811054":{
        "name":"hemanth",
        "department":"cse",
    },
}

roll_number = input("Enter roll number: ")
if roll_number in students:
    student = students[roll_number]
    print(f"Name: {student['name']}")
    print(f"Department: {student['department']}")
else:
    name = input("Enter name: ")
    department = input("Enter department: ")
    students[roll_number] = {"name": name, "department": department}
    print("New student added.")
    print(f"Name: {name}")
    print(f"Department: {department}")